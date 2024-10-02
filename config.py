# Thanks For: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/ramadhani892/RamPyro-Bot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/ramsupportt


from distutils.util import strtobool
from os import getenv

from dotenv import load_dotenv

load_dotenv(".env")


ALIVE_EMOJI = getenv("ALIVE_EMOJI", "🔥")
ALIVE_LOGO = getenv("ALIVE_LOGO", "https://telegra.ph/file/d370f45bf3ff8fa0cba8f.jpg")
ALIVE_TEKS_CUSTOM = getenv("ALIVE_TEKS_CUSTOM", "Haii tod. Ferdi-Userbot aktif!")
API_HASH = getenv("API_HASH", "5d7858e035599aa080d65e14e5e34d4d")
API_ID = getenv("API_ID", "22355402")
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001692751821]
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID", "4556709976")
BOT_TOKEN = getenv("BOT_TOKEN", "7463102988:AAFQp16pBbCSchNMsH6Yd-sAtGLvvH0Q8cs")
BOT_VER = "1.0.7"
BRANCH = getenv("BRANCH", "main")
CH_SFS = getenv("CH_SFS", "Galerifsyrl")
IG_ALIVE = getenv("IG_ALIVE", "fsyrl_")
CHANNEL = getenv("CHANNEL", "userbotch")
CMD_HANDLER = getenv("CMD_HANDLER", ".")
CMD_HNDLR = CMD_HANDLER
ID_OWNER = getenv("ID_OWNER", "7083782157")
DB_URL = getenv("DATABASE_URL", "postgresql://evadb_owner:l2d8PojNOtAn@ep-misty-brook-a5stybd0.us-east-2.aws.neon.tech/evadb?sslmode=require")
GIT_TOKEN = getenv("GIT_TOKEN", "")
GROUP = getenv("GROUP", "BestieVirtual")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
PMPERMIT_PIC = getenv("PMPERMIT_PIC", None)
OPENAI_API_KEY = getenv("OPENAI_API_KEY", "")
PM_AUTO_BAN = strtobool(getenv("PM_AUTO_BAN", "False"))
REPO_URL = getenv("REPO_URL", "https://github.com/GeezRampy/Ram-Pyro")
STRING_SESSION1 = getenv("STRING_SESSION1", "BQFVHcoAQUK5hyNuxBaoPzrYKTfXE2Z_m6Ze2sI_KiSAjUzZzZrBuBnryoCab2EHb-Sg23uruVUphfYQSH0fRtuu6AZEGQ8xooTiVmfTOEOpXzF70JnQD7megmOcigpV0_Eq303aFRZcUYECyWgz2WUPLrMPVVuoQk2DRPm8DSBpdDytzQ25vgnSrn9v8VdijYnBPHdO0qOcgxe9JC_0PjvLGlC23drqpvfvlzmDJ1RpF5Sxp0iAK9RPMTgY4r8wCNlNurKnqwUfXN9DXlAUiibDLIyOCm3eFYWSfTVqPPxK8DN2_4nNhl5wAiDRK7id9MwbP12kq4CMLeuYl_qDkx_2TxXwOgAAAAGmOfANAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
