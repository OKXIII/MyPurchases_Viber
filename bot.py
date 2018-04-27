from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration

bot_configuration = BotConfiguration(
	name='MyPurchases',
	avatar='http://viber.com/avatar.jpg',
	auth_token='47a71cffbce7d0eb-bb788620e6861ddf-7df845e6e386c7f4'
)
viber = Api(bot_configuration)