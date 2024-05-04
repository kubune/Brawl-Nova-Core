import nextcord
from nextcord.ext import commands
from colorama import Fore as set_color
from configuration import *

class Nova(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="nova!",
            intents=nextcord.Intents.default(),
        )
        self.initial_extentions = [
            "misc.hello"
        ]
    cogs = "cogs."
     
    async def on_ready(self):
        print(set_color.GREEN + f'{self.user} connected!' + set_color.RESET)
        await self.change_presence(activity=nextcord.Streaming(
    name=f"{status}", url=f"{status_url}"))
        print(set_color.YELLOW + f"Set status to: \"{status}\" with URL: \"{status_url}\"" + set_color.RESET)
        print(set_color.CYAN + "Trying to synchronize coommands..." + set_color.RESET)
        try:
            synced = await bot.tree.sync()
            print(set_color.CYAN + f"Synced {len(synced)} slash command(s)" + set_color.RESET)
        except Exception as Error:
            print(set_color.RED + "An error occured while trying to synchronize commands..." + set_color.RESET)
            print(Error)
        print(set_color.GREEN + 'Nova has started successfully!' + set_color.RESET)

    async def setup_hook(self):
        for ext in self.initial_extentions:
            try:
                await self.load_extension(self.cogs + ext)
                print(set_color.GREEN + f'Loaded command: {ext}' + set_color.RESET)
            except Exception as error:
                print(error)



bot = Nova()
bot.run(token)