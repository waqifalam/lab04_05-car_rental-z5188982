# USER CLASS

class User:
	_id = 1;

	def __init__(self, username, password, booking):
		self._userID = self._generateID()
		self._username = username
		self._password = password
		self._bookingList = []


	#userID
	@property	
	def userID():
		return self. userID
	
	@userID.setter
	def userID(self, userID):
		self.userID = userID

	#USERNAME
	@property
	def username():
		return self._username

	#@username refers to the def username in line below
	@username.setter
	def username(self, username):
		self._username = username

	#PASSWORD
	@property
	def password():
		return self._password

	@password.setter
	def password(self, password):
		self._password = password

	@property
	def bookinglist():
		return self._bookingList

	def addBooking(self, booking):
		self.bookingList.append(booking)
	

	def _generateID():
		User._userID+=
		return User._userID
		

class Customers(User):
	def __init__(self, username, password, booking):
		User.__init__(self, username, password, booking)

class Staff(User):
	def __init__(self, username, password, booking, userType):
		User.__init__(self, username, password, booking)

	@property
	def newCar(make, model etc):
		return self._newCar
	


class Managers(Staff):
	def __init__(self, username, password, booking, userType):
		User.__init__(self, username, password, booking)

	@property
	def generateReport():
		return Car._totalBookings






