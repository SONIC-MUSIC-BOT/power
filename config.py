from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "360"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/c27f34d40b4664d1a4db7.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/c27f34d40b4664d1a4db7.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Exppower")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/K8XXX")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2038302618").split()))


CHANNEL_SUDO = getenv(
    "CHANNEL_SUDO", "K8XXX"
)

YAFA_NAME = getenv(
    "YAFA_NAME", "سورس باور"
)

YAFA_CHANNEL = getenv(
   " YAFA_CHANNEL", "https://t.me/K8XXX" 
)


FAILED = "https://telegra.ph/file/c27f34d40b4664d1a4db7.jpg"
