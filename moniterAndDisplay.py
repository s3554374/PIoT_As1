from sense_hat import SenseHat
from time import sleep
import json
import temperature as temperature
import calibration as calibrate

sense = SenseHat()
sense.low_light = True
temperature_range = []
current_temperature = 0

def set_up_readings(temperature_data):
	temperature_range.append(temperature.Temperature
		(0,temperature_data["cold_max"], 0,0,255))

	temperature_range.append(temperature.Temperature
		(temperature_data["comfortable_min"],
		temperature_data["comfortable_max"], 0,255,0))

	temperature_range.append(temperature.Temperature
		(temperature_data["hot_min"],100, 255,0,0))

	measure_temperature(temperature_range)


def measure_temperature(temperature_range):
	while True:

	current_temperature = calibrate.get_temperature(sense);
	print(current_temperature)
	
	for x in temperature_range:
		if (current_temperature < x.get_maximum() and current_temperature > x.get_minimum()):
			x.display_colour(sense)

	sleep(10)


load_error = 'Error'

try:
	with open ("config.json") as data:
		temperature_data = json.load(data)
except IOError:
	sense.show_message(load_error)
	print(load_error)
else:
	set_up_readings(temperature_data)
