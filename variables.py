import json
import os


def get_user_list(config, key):
    with open("{}/Champubot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


class Config(object):
    # Configuration class for the bot

    # Enable or disable logging
    LOGGER = True

    # <================================================ REQUIRED ======================================================>
    # Telegram API configuration
    API_ID = 26544005 # Get this value from my.telegram.org/apps
    API_HASH = "66f6221e5ce9109827b50eaf3d105025"

    # Database configuration (PostgreSQL)
    DATABASE_URL = "postgresql://postgres.jocwxwsjzbhzevpifnnl:KontolXD#123@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres"

    # Event logs chat ID and message dump chat ID
    EVENT_LOGS = -1002554488354
    MESSAGE_DUMP = -1002554488354

    # MongoDB configuration
    MONGO_DB_URI = "mongodb+srv://wtfbruh:KontolXD#123@fsub.brzgete.mongodb.net/?retryWrites=true&w=majority&appName=fsub"

    # Support chat and support ID
    SUPPORT_CHAT = "https://t.me/lokontolya"
    SUPPORT_ID = -1002818541265

    # Database name
    DB_NAME = "Jonathan"

    # Bot token
    TOKEN = "7718133895:AAFnUWI0MPBISInsWYFKXlJ_3NBah1mSUFk"  # Get bot token from @BotFather on Telegram

    # Owner's Telegram user ID (Must be an integer)
    OWNER_ID = 5870285414
    # <=======================================================================================================>

    # <================================================ OPTIONAL ======================================================>
    # Optional configuration fields

    # List of groups to blacklist
    BL_CHATS = [-1002453146086]

    # User IDs of sudo users, dev users, support users, tiger users, and whitelist users
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    DEMONS = get_user_list("elevated_users.json", "supports")
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")

    # Toggle features
    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True

    # Modules to load or exclude
    LOAD = []
    NO_LOAD = []

    # Global ban settings
    STRICT_GBAN = True
    BAN_STICKER = (
        "CAACAgUAAxkBAAEGWC5lloYv1tiI3-KPguoH5YX-RveWugACoQ4AAi4b2FQGdUhawbi91DQE"
    )

    # Temporary download directory
    TEMP_DOWNLOAD_DIRECTORY = "./"
    # <=======================================================================================================>


# <=======================================================================================================>


class Production(Config):
    # Production configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True


class Development(Config):
    # Development configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True
