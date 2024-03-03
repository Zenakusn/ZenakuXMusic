from Zenaku.core.bot import ZenakuBot
from Zenaku.core.dir import dirr
from Zenaku.core.git import git
from Zenaku.core.userbot import Userbot
from Zenaku.misc import dbb, heroku

from .logging import LOGGER

git()


dirr()

dbb()

heroku()

# Clients
app = ZenakuBot()

userbot = Userbot()


from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
