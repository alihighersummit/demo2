import os
from dotenv import load_dotenv

class Constants:
    load_dotenv(".env")
    REST_SERVER_PORT = os.getenv('REST_SERVER_PORT')
    REST_SERVER_API_ADDRESS = os.getenv('REST_SERVER_API_ADDRESS')
