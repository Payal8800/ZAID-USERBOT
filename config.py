import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "6435225")) #optional
API_HASH = getenv("API_HASH", "") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6205439087").split()))
OWNER_ID = int(getenv("OWNER_ID"))
MONGO_URL = getenv("MONGO_URL")
BOT_TOKEN = getenv("BOT_TOKEN", "5995985023:AAFD8aaHmAwKDI7ltrlbTDTQCpCp0K--9Ds")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://telegra.ph/file/3c52a01057865f7511168.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQBiMZkArsvnZX3Yx2xP1YE6sYkl_Pobrr1NQfaTW4c5YlumCNZS97GyUgSCQaiAu7M4YXP06lgoWiEgSFpUmwRSFc_80Lwomkne6N26CcCteWIn8WF9ikXahKJkGs46XKG09rambElY7qlfTm5Tsd7NGC7tSS5bPYsuxX-Nm8QKatpq3DAi8pSFT8izDHVi6pNPxQQ5RHbPHhPs9Ww_-63cMm-yWK_qmft1eJ_w3Lad1en-R696bY3uRQAnGjazYMCynJPg4XAlAHR0AVzHj0SEx-Res62VcsMAF-yGAPTZ9F69o6vlH9-rfx3zG-s3ie1bmSXj4LuE0DGIxblzZGCZ97rgsQAAAAFx33xvAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
