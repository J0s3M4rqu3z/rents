from rents import rents

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
