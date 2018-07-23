import os
import sys
import requests
import dill

from pprint import pprint
from xboxapi import Client


class UserProfile(object):
	"""The Current Gamers Profile"""

	gamer_saved_profile = 'gamer.pkl'
	timeout = 30

	def __init__(self, api_key='32d2c125d1897a51adce86a13ffaf037ee713581', lang='en-CA'):
		"""Get the current users UserProfile"""

		self.api_key = api_key
		self.lang = lang
		self.timeout = UserProfile.timeout

		get_new_gamer = False

		if get_new_gamer or not os.path.isfile(UserProfile.gamer_saved_profile) or not os.stat(
				UserProfile.gamer_saved_profile).st_size:
			gamertag = 'TheWhiteR4bbitt'
			pprint('Writing file')
			try:
				client = Client(api_key=self.api_key, timeout=self.timeout, lang=self.lang)
				self.gamer_profile = client.gamer(gamertag=gamertag)

				with open(UserProfile.gamer_saved_profile, 'wb') as file:
					dill.dump(self.gamer_profile, file)
					pprint('Successfully wrote gamer to file')
			except requests.exceptions.Timeout:
				e = sys.exc_info()[0]
				pprint('Error: %s' % e)
		else:
			pprint('Reading file')
			with open(UserProfile.gamer_saved_profile, 'rb') as file:
				self.gamer_profile = dill.load(file)
				pprint('Successfully read gamer from file')

		self.xuid = self.get_player_xuid()
		pprint(self.get_profile())
		# pprint(self.get_profile().gamerscore)
		pprint(self.get_latest_xboxone_games())
		pprint(self.get_achievements())

	def get_profile(self):
		return self.gamer_profile.get('profile')

	def get_player_xuid(self):
		return self.gamer_profile.fetch_xuid()

	def get_latest_xboxone_games(self):
		return self.gamer_profile.get(method=self.xuid, term='latest-xboxone-games')

	def get_achievements(self):
		return self.gamer_profile.get(method=self.xuid, term='achievements')

	def dump(self, obj):
		for attr in dir(obj):
			print(type(attr))
			if type(attr) is obj:
				self.dump(attr)
			else:
				print("obj.%s = %r" % (attr, getattr(obj, attr)))




UserProfile()