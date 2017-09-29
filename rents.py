import datetime as dt
import time
import math


def Hour(ob):
	return math.ceil((ob.close-ob.start).seconds/60)*5*ob.discount

def Day(ob):
	return ((ob.close.date()-ob.start.date()).days)*20*ob.discount

def Week(ob):
	return math.ceil(((ob.close.date()-ob.start.date()).days)/7)*60*ob.discount

class rents():
	def __init__(self,kind='Hour',family=False):
		self.kind = kind
		self.family=family
		self.start = dt.datetime.now()- dt.timedelta(days=7)
		self.amount=0
		self.discount= 0.7 if family else 1
		print('The rent has begun at '+str(self.start))

	def charge(self):
		options = {
			'Hour':Hour,
			'Day':Day,
			'Week':Week
		}
		self.close = dt.datetime.now()
		self.amount =options[self.kind](self)
		print(self.amount)
		return self.amount

class register_rent():
	def __init__(self):
		self.rents_register = []

	def register(self,quantity=1,kinds=['hour']):
		response = []
		family = True if (quantity>=3 and quantity<=5) else False
		for i in range(quantity):
			self.rents_register.append(rents(kind=kinds[i-1] ,family=family))
			response.append(len(self.rents_register)-1)
		return response

	def toCharge(self,register):
		self.rents_register[register].charge()
