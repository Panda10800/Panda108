import os
from os import getenv
from dotenv import load_dotenv
from OWNER import BOT_TOKEN, OWNER, OWNER_NAME, DATABASE, CHANNEL, GROUP, LOGS, VIDEO

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
user = {}
call = {}
dev = {}
logger = {}
logger_mode = {}
botname = {}
appp = {}
helper = {}



API_ID = int(getenv("API_ID", "1947348611"))
API_HASH = getenv("API_HASH", "98dcc3be2aaa04311c8f27350abe80a3")
BOT_TOKEN = BOT_TOKEN
MONGO_DB_URL = DATABASE
OWNER = OWNER
OWNER_NAME = OWNER_NAME
CHANNEL = CHANNEL
GROUP = GROUP
LOGS = LOGS
VIDEO = VIDEO