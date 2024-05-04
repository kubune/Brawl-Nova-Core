import nextcord
from nextcord.ext import commands
from colorama import Fore as set_color
from configuration import *
intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="nova!",
            intents=intents
)
initial_extentions = [
            "misc.hello"
            ]

cogs = "cogs."
    
@bot.event
async def on_ready():
    print(set_color.GREEN + f'{bot.user} connected!' + set_color.RESET)
    game = nextcord.Game(name=status)
    await bot.change_presence(status=nextcord.Status.online, activity=game)
    print(set_color.YELLOW + f"Set status to: \"{status}\"" + set_color.RESET)
    print(set_color.GREEN + 'Nova has started successfully!' + set_color.RESET)


for ext in initial_extentions:
    try:
        bot.load_extension(cogs + ext)
        print(set_color.LIGHTYELLOW_EX + f'Loaded command: {ext}' + set_color.RESET)
    except Exception as error:
        print(error)
bot.run(token)