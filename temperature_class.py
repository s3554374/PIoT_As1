class Temperature:
	__min_temp = 0
	__max_temp = 100
	__blue = 0
	__green = 0
	__red = 0

def __init__ (self, min, max, red, green, blue):
	self.__min_temp = min
	self.__max_temp = max
	self.__blue = blue
	self.__green = green
	self.__red = red

def get_minimum(self):
	return self.__min_temp

def get_maximum(self):
	return self.__max_temp

def display_colour(self, sense):
	sense.clear((self.__blue,self.__green,self.__red))
