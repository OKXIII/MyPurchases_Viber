from flask import Flask, request, Response, render_template
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages.text_message import TextMessage
from viberbot.api.viber_requests import ViberConversationStartedRequest
from viberbot.api.viber_requests import ViberFailedRequest
from viberbot.api.viber_requests import ViberMessageRequest
from viberbot.api.viber_requests import ViberSubscribedRequest
from viberbot.api.viber_requests import ViberUnsubscribedRequest

import time
import logging
import sched
import threading

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

app = Flask(__name__)
viber = Api(BotConfiguration(
  name='MyPurchases',
  avatar='https://github.com/OKXIII/MyPurchasesBot/blob/master/MyPurchasesBot.jpg?raw=true',
  auth_token='490fdf7a8567d79f-55497f0c7abb8e34-c86174030e8599c0'
))


#@app.route('/', methods=['POST'])
@app.route('/', methods=['GET'])
def incoming():
	logger.debug("received request. post data: {0}".format(request.get_data()))
	print ('URA!')

	if not viber.verify_signature(request.get_data(), request.headers.get('X-Viber-Content-Signature')):
		return Response(status=403)
	print ('URA1')

	# this library supplies a simple way to receive a request object
	viber_request = viber.parse_request(request.get_data())
	print ('URA2')

	if isinstance(viber_request, ViberMessageRequest):
		message = viber_request.message
		# lets echo back
		viber.send_messages(viber_request.sender.id, [
			message
		])
		print('URA3')

	elif isinstance(viber_request, ViberSubscribedRequest):
		viber.send_messages(viber_request.get_user.id, [
			TextMessage(text="thanks for subscribing!")
		])
	elif isinstance(viber_request, ViberFailedRequest):
		logger.warn("client failed receiving message. failure: {0}".format(viber_request))
	print ('URA4')

	return Response(status=200)
#	return render_template('index.html')

def set_webhook(viber):
	print ('Set_webhook')
	viber.set_webhook('https://oktestbot.herokuapp.com:443/')
#	viber.set_webhook('https://oktestbot.herokuapp.com:8443/')



if __name__ == "__main__":
#	scheduler = sched.scheduler(time.time, time.sleep)
#	scheduler.enter(5, 1, set_webhook, (viber,))
#	t = threading.Thread(target=scheduler.run)
#	t.start()
	set_webhook(viber)
	print ('WEBHOOK')
	context = ('server.crt', 'server.key')
	app.run(host='0.0.0.0', port=443, debug=True, ssl_context=context)