from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration

bot_configuration = BotConfiguration(
	name='MyPurchases',
	avatar='https://github.com/OKXIII/MyPurchasesBot/blob/master/MyPurchasesBot.jpg?raw=true',
#	auth_token='47a71cffbce7d0eb-bb788620e6861ddf-7df845e6e386c7f4'
	auth_token='490fdf7a8567d79f-55497f0c7abb8e34-c86174030e8599c0'
)
viber = Api(bot_configuration)