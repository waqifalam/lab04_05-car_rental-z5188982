class booking():
    _id = -1
    
    def __init__(self, carID, startDate, rentalPeriod, totalPrice, insurance, customerAge, customerName, licenseNumber, emailAddress):
        self._bookingID = self._generateID
        self._carID = carID
        self._startDate = startDate
        self._rentalPeriod = rentalPeriod
        self._totalPrice = totalPrice
        self._insurance = insurance
        self._customerAge = customerAge
        self._customerName = customerName
        self._licenseNumber = licenseNumber
        self._emailAddress = emailAddress

    @property
    def carID():
        return self._carID

    @carID.setter
    def carID(self, carID):
        self._carID = carID

    @property
    def startDate():
        return self._startDate
    
    @startDate.setter
    def startDate(self, startDate):
        self.startDate = startDate

    @property
    def rentalPeriod():
        return self._rentalPeriod
    
    @rentalPeriod.setter
    def rentalPeriod(self, rentalPeriod):
        self._rentalPeriod = rentalPeriod

    @property
    def totalPrice():
        return self._totalPrice

    @totalPrice.setter
    def totalPrice(self, totalPrice):
        self._totalPrice = totalPrice

    @property
    def insurance():
        return self._insurance

    @insurance.setter
    def insurance(self, insurance):
        self._insurance = insurance

    @property
    def customerAge():
        return self._customerAge
    
    @customerAge.setter
    def customerAge(self, customerAge):
        self._customerAge = customerAge

    @property
    def customerName():
        return self._customerName

    @customerName.setter
    def customerName(self, customerName):
        self._customerName = customerName

    @property
    def licenseNumber():
        return self._licenseNumber
    
    @licenseNumber.setter
    def licenseNumber(self, licenseNumber):
        self._licenseNumber = licenseNumber

    @property
    def emailAddress():
        return self._emailAddress

    @emailAddress.setter
    def emailAddress(self, emailAddress):
        self._emailAddress = emailAddress
    

    def _generateID():
        Car._id+=
        return Car._id
