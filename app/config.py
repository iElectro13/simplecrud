class Config:
    DEBUG = True
    """Flask config class."""
    SECRET_KEY = 'Secret ideas'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../ideas.db'
    SQLALCHEMY_TRACK_NOTIFICATIONS = False
    