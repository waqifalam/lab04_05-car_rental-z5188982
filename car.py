# look up abstract classes in python
class Car(ABC):
    _id = -1;
    _totalBookings = []
    
    def __init__(self, make, model, year, registration, bookingInfo,vehicleType,rate):
        self._carID = self._generateID()
        self._make = make
        self._model = model
        self._year = year
        self._registration = registration
        self._bookingInfo = bookingInfo
        self._vehicleType = vehicleType
        self._rate = rate
        self._bookingList = []

    @property
    def carID():
        return self._carID

    @carID.setter
    def carID(self, carID)
        self._carID = carID

    @property
    def make():
        return self._make

    @make.setter
    def make(self,make):
        self._make = make

    @property
    def model():
        return self._model

    @model.setter
    def model(self, model):
        self._model = model

    @property
    def year():
        return self._year

    @year.setter
    def year(self, year)
        self._year = year

    @property
    def registration():
        return self._registration

    @registration.setter
    def registration(self, registration):
        self._registration = registration

    @property
    def bookingInfo():
        return self._bookingInfo

    @bookingInfo.setter(self, bookingInfo):
        self._bookingInfo = bookingInfo 
        Car._totalBookings.append(bookingInfo)
    @property
    def _totalBookings():
        return Car._totalBookings
        
    @property
    def vehicleType():
        return self._vehicleType

    @vehicleType.setter
    def vehicleType(self, vehicleType):
        self._vehicleType = vehicleType

    @property
    def rate():
        return self._rate

    @rate.setter
    def rate(self, rate):
        self._rate = rate

    def _generateID():
        Car._id+=
        return Car._id

class SmallCar(Car):
    def __init__(self, make, model, year, registration, bookingInfo,vehicleType,rate):
        Car.__init__(self,make,model,year,registration,bookingInfo,"small",rate)

class MediumCar(Car):
    def __init__(self, make, model, year, registration, bookingInfo,vehicleType,rate):
        Car.__init__(self,make,model,year,registration,bookingInfo,"medium", rate)

class LargeCar(Car):
    def __init__(self, make, model, year, registration, bookingInfo,vehicleType,rate):
        Car.__init__(self,make,model,year,registration,bookingInfo,"large", rate)

class PremiumCar(Car):
    def __init__(self, make, model, year, registration, bookingInfo, vehicleType, rate):
        Car.__init__(self,make,model,year,registration,bookingInfo,"large", rate)
    
