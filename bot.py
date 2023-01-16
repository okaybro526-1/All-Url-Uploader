import os
from pyrogram import Client, idle
from Uploader.config import Config
import logging
from pyrogram.raw import functions, types
from pyromod import listen


STATUS=Config.STATUS

USER=Config.USER
bot = Client(
    "InstaSessibon",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    workers=50,
    plugins=dict(root="plugins")
    )

async def main():
    async with bot:
        await bot.download_media(Config.INSTA_SESSIONFILE_ID, file_name=f"./{Config.USER}")
        Config.L.load_session_from_file(USER, filename=f"./{USER}")
        STATUS.add(1)

if Config.INSTA_SESSIONFILE_ID:
    bot.run(main())
    
bot.start()

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

logging.getLogger("pyrogram").setLevel(logging.WARNING)


if __name__ == "__main__":

    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)

    plugins = dict(root="Uploader")
    Uploadbot = Client("All-Url-Uploader",
                       bot_token=Config.BOT_TOKEN,
                       api_id=Config.API_ID,
                       api_hash=Config.API_HASH,
                       plugins=plugins)
    logger.info("Bot Started :)")
    Uploadbot.run()
    idle()
    logger.info("Bot Stoped ;)")
