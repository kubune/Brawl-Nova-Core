import nextcord
from nextcord.ext import commands
from colorama import Fore as set_color
import arrow
import requests
apitoken = "" #implement your own config 

class QuickPlayer(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @nextcord.slash_command(
        name =  "quickplayer",
        description = "Check desired player tag at the speed the light!"
    )

    async def template(
        self,
        interaction: nextcord.Interaction,
        playertag: str
    ) -> None:
        user = interaction.user
        print(set_color.LIGHTBLUE_EX + f"Log: {user.name}(ID: {user.id})(Guild: {interaction.guild.name}(ID: {interaction.guild_id})) used /quickplayer at {arrow.now().format('DD/MM/YYYY HH:mm:ss')}" + set_color.RESET)
        
        playertag = playertag.upper()
        if playertag[0] == '#':
            playertag = playertag[1:]
        headers = {"Authorization": "Bearer {}".format(apitoken)}
        response = requests.get(headers=headers, url="https://api.brawlstars.com/v1/players/%23{}".format(playertag)).json()
        embed = nextcord.Embed()
        embed.title = f"{response['name']}'s profile"
        embed.color = 0x2B2D31
        embed.set_thumbnail(url="https://cdn-old.brawlify.com/profile/{}.png".format(str(response['icon']['id'])))
        embed.description = f"Tag: {response['tag']}\nTrophies🏆: {response['trophies']}/{response['highestTrophies']}\n3v3 wins: {response['3vs3Victories']}\nSolo wins: {response['soloVictories']}\nDuo wins: {response['duoVictories']}\n" 
        try:
            embed.set_footer(icon_url=user.avatar.url, text=f"Command used by {user.name}")
        except:
            embed.set_footer(icon_url=self.bot.user.avatar.url, text=f"Command used by {user.name}")
        await interaction.response.send_message(embed=embed)

def setup(bot: commands.Bot) -> None:
    bot.add_cog(
        QuickPlayer(bot)
    )
    
