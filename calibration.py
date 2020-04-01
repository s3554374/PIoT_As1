# 05_sensehat_calibration.py
import os

# Get CPU temperature.
def get_cpu_temp():
	res = os.popen("vcgencmd measure_temp").readline()
	return float(res.replace("temp=","").replace("'C\n",""))

# Use moving average to smooth readings.
def get_smooth(x):
	if not hasattr(get_smooth, "t"):
		get_smooth.t = [x,x,x]

	get_smooth.t[2] = get_smooth.t[1]
	get_smooth.t[1] = get_smooth.t[0]
	get_smooth.t[0] = x

	return (get_smooth.t[0] + get_smooth.t[1] + get_smooth.t[2]) / 3

def get_temperature(sense):
	t1 = sense.get_temperature_from_humidity()
	t2 = sense.get_temperature_from_pressure()
	t_cpu = get_cpu_temp()
	h = sense.get_humidity()
	p = sense.get_pressure()

	# Calculates the real temperature compesating CPU heating.
	t = (t1 + t2) / 2
	t_corr = t - ((t_cpu - t) / 1.5)
	t_corr = get_smooth(t_corr)

	return t_corr
