import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID","25961801"))
API_HASH = getenv("API_HASH","c9d39e5cba88255416aad52f0d0e1cd8")
BOT_TOKEN = getenv("BOT_TOKEN","")
MONGO_DB_URI = getenv("MONGO_DB_URI", "")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "9999"))
LOGGER_ID = int(getenv("LOGGER_ID", "-1002011084696"))
BOTADDLOGS = int(getenv("BOTADDLOGS", "-1002011084696")) # LOGGER_ID Id Also Use No Problem
GBAN_LOGS = int(getenv("GBAN_LOGS", "-1002081933358"))
OWNER_ID = int(getenv("OWNER_ID", 6942607332))
OWNER = int(getenv("OWNER", 7031870310))
OWNER_USERNAME = getenv("OWNER_USERNAME","imStubborn0")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
UPSTREAM_REPO = getenv("UPSTREAM_REPO","https://github.com/Aashu1572/MUSIC_NORMAL")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN",None)
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/PDF_Factory")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Student_Studys_Group")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "5400"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", 7000))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", 7000))
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "9999")) 
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2a230af10e0a40638dc77c1febb47170")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "7f92897a59464ddbbf00f06cd6bda7fc")
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "3000"))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 5242880000))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 5242880000))
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
AMBOT = [
    "🔎",
    "🔍",
    "🧪",
    "ᴘʟꜱ ᴡᴀɪᴛ..",
    "ᴘʀᴏᴄᴇꜱꜱɪɴɢ..",
]

START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/799c150177b85a00f81f4.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/c2529e97e8cfece4e405f.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/be7f1a66e15450b65fd63.jpg"
STATS_IMG_URL = "https://telegra.ph/file/8e2b7bd208e40476b2f7c.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/48f39202823b358203234.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/e575ae40d6635250974e1.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/03efec694e41e891b29dc.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/4dc854f961cd3ce46899b.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
