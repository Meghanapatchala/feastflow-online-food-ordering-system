import os
from dotenv import load_dotenv

# Load key-values from a .env file if available
load_dotenv()

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "feastflow-secure-premium-key-2026")
    
    # DB settings
    DB_USER = os.environ.get("DB_USER", "root")
    DB_PASSWORD = os.environ.get("DB_PASSWORD", "")
    DB_HOST = os.environ.get("DB_HOST", "localhost")
    DB_PORT = os.environ.get("DB_PORT", "3306")
    DB_NAME = os.environ.get("DB_NAME", "food_ordering")
    
    MYSQL_URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    SQLITE_URI = "sqlite:///" + os.path.join(os.path.abspath(os.path.dirname(__file__)), "food_ordering.db")
    
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    if not SQLALCHEMY_DATABASE_URI:
        if os.environ.get("USE_MYSQL", "False").lower() == "true":
            SQLALCHEMY_DATABASE_URI = MYSQL_URI
        else:
            SQLALCHEMY_DATABASE_URI = SQLITE_URI
            
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), "static", "images")
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024