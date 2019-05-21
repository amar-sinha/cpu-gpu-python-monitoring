import RPi.GPIO as GPIO
import os, time, sys
from datetime import date

#TEMPERATURE SENSORS

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

room_temp_sensor = '/sys/bus/w1/devices/28-05178024faff/w1_slave'
temp_in_sensor = '/sys/bus/w1/devices/28-0516a51be9ff/w1_slave'
temp_out_sensor = '/sys/bus/w1/devices/28-05178027caff/w1_slave'

def temp_raw(sensor): #retrieves temperature sensor data from devices storage
	f = open(sensor, 'r')
	lines = f.readlines()
	f.close()
	return lines

def read_temp(sensor): #reads the temperature from the data retrieved via temp_raw
	lines = temp_raw(sensor)
	while lines[0].strip()[-3:] != 'YES': #removes unnecessary information from data
		lines = temp_raw()
	temp_output = lines[1].find('t=') #finds temperature indicated by presence of 't='
	if temp_output != -1: #checks for invalid temperature
		temp_string = lines[1].strip()[temp_output+2:] #strips unnecessary information and leaves on temperature
		temp_c = float(temp_string) / 1000.0 #converts from string to float and adjusts decimals to get Celsius
		strtemp_c = str(temp_c) #strings the Celsius temperature
		strtemp_f = str(temp_c * 9.0 / 5.0 + 32.0) #converts to Fahrenheit and strings the temperature
		return strtemp_f

#FLOW SENSOR

FLOW_SENSOR = 23 #defines the pin used on the RPi

GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down=GPIO.PUD_UP) #sets up pin as input with pull up resistor

global count
count = 0

def countPulse(channel): #function defined for counting pulses in sensor
	global count
	count += 1

GPIO.add_event_detect(FLOW_SENSOR, GPIO.FALLING, callback = countPulse)

def flow():
	global count
	time.sleep(1)
	flowrate1 = (count*60)/7.5 #conversion rate defined by datasheet
	flowrate2 = flowrate1 * (0.264172/60) #converts to gallons per minute
	flowtext = str(flowrate2) #strings final data
	count = 0 #resets the pulse count
	return(flowtext)

f = open('temperature.txt', 'w').close() #clears the data text file for new use
header = "Date & Time, Room Temperature (F), Temperature In (F), Temperature Out (F), Flow Rate (GPM)" #adds headers to the data text file
f = open("temperature.txt", "w") #opens file for writing
f.write(header) #writes the headers to the file

while True: #writes data to the file in a continuous loop
	time_new = time.time() + 12
	while time.time() <= time_new:
		continue
	with open("temperature.txt", "a") as f: #use "a" to keep adding the file and not rewrite over data
		text = str("(" + str(date.today()) +  ", " + time.strftime("%H:%M:%S") + ")"  + ", " + read_temp(room_temp_sensor) + ", " + read_temp(temp_in_sensor) + ", " + read_temp(temp_out_sensor) + ", " + flow())
		f.write('\n')
		f.write(text)
	f.close()
