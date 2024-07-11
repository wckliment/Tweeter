# !!START
import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", 'secretkey123')
    # define any other secret environment variables here

# !!END
