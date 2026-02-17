import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Telegram API
API_ID = int(getenv("API_ID", "0"))
API_HASH = getenv("API_HASH", "")

# Bot token
BOT_TOKEN = getenv("BOT_TOKEN", "")

# MongoDB URL
MONGO_DB_URI = getenv("MONGO_DB_URI", "")

# Limits
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 360))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", 5400))

# Logger & Owner
LOGGER_ID = int(getenv("LOGGER_ID", "0"))
OWNER_ID = int(getenv("OWNER_ID", "0"))

# Heroku deployment
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# Git & upstream repo
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Rq7mg/Vancedkiyici")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

# Support links
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/kycmusicdestek")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/kiyicitayfaa")

# Assistant behavior
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))

# Spotify credentials
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

# Playlist & file size limits
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 314572800))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 3221225472))

# Pyrogram string sessions
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

# Misc
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []
confirmer = {}

# Images
START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/Panda-06-24-7")
PING_IMG_URL = getenv("PING_IMG_URL", "https://telegra.ph/Panda-06-24-7")
PLAYLIST_IMG_URL = "https://telegra.ph/Panda-06-24-7"
STATS_IMG_URL = "https://telegra.ph/Panda-06-24-7"
TELEGRAM_AUDIO_URL = "https://telegra.ph/Panda-06-24-7"
TELEGRAM_VIDEO_URL = "https://telegra.ph/Panda-06-24-7"
STREAM_IMG_URL = "https://telegra.ph/Panda-06-24-7"
SOUNCLOUD_IMG_URL = "https://telegra.ph/Panda-06-24-7"
YOUTUBE_IMG_URL = "https://telegra.ph/Panda-06-24-7"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/Panda-06-24-7"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/Panda-06-24-7"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/Panda-06-24-7"

# Helpers
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = time_to_seconds(f"{DURATION_LIMIT_MIN}:00")
SONG_DOWNLOAD_DURATION_LIMIT = time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")

# URL validation
if SUPPORT_CHANNEL and not re.match(r"(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - SUPPORT_CHANNEL url is wrong. Must start with https://")
if SUPPORT_CHAT and not re.match(r"(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] - SUPPORT_CHAT url is wrong. Must start with https://")
