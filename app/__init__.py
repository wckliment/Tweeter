# !!START
import random
from flask import Flask, render_template, redirect, url_for, request, flash
from .config import Config
from .tweets import tweets
from .Forms.form import TweetForm
from datetime import datetime




app = Flask(__name__)

app.config.from_object(Config)
# !!END


@app.route('/')
def index():
    tweet = random.choice(tweets)
    return render_template('index.html', tweet=tweet)

@app.route('/feed')
def feed():
    sorted_tweets = sorted(tweets, key=lambda x: datetime.strptime(x['date'], "%m/%d/%y"), reverse=True)
    return render_template('feed.html', tweets=sorted_tweets)

@app.route('/new', methods=['GET', 'POST'])
def new_tweet():
    form = TweetForm()
    if form.validate_on_submit():
        new_tweet = {
            "id": len(tweets) + 1,
            "author": form.author.data,
            "tweet": form.tweet.data,
            "likes": random.randint(0, 1000),  # Random likes for demonstration purposes
            "date": datetime.now().strftime("%m/%d/%y")  # Consistent date format
        }
        tweets.append(new_tweet)
        flash('Tweet created successfully!', 'success')
        return redirect(url_for('feed'))
    if form.errors:
        flash('Error in form submission. Please check the fields and try again.', 'danger')
    return render_template('new_tweet.html', form=form)

@app.route('/like/<int:tweet_id>')
def like_tweet(tweet_id):
    tweet = next((t for t in tweets if t['id'] == tweet_id), None)
    if tweet:
        tweet['likes'] += 1
    return redirect(url_for('feed'))

@app.route('/unlike/<int:tweet_id>')
def unlike_tweet(tweet_id):
    tweet = next((t for t in tweets if t['id'] == tweet_id), None)
    if tweet and tweet['likes'] > 0:
        tweet['likes'] -= 1
    return redirect(url_for('feed'))

if __name__ == '__main__':
    app.run(debug=True)
