import sys
import re

inputfile = open(sys.argv[1],'r')
outputfile = open(sys.argv[1].replace("in","out"),'w')

testcases = int(inputfile.readline())

for i in range(0, testcases):
	test = inputfile.readline().split(" ")
	dest = int(test[0])
	horses = int(test[1])

	max_time = -1.0
	max_speed = 0
	for horse in range(0,horses):
		horse_info = inputfile.readline().split(" ")
		curr_km = int(horse_info[0])
		speed = int(horse_info[1])

		time = ((dest-curr_km) * 1.0) / (speed * 1.0)
		if time > max_time:
			max_time = time
			max_speed = speed

	

	annie_speed =  (dest*1.0)/max_time

	print "ANNIE SPEED: %f" % annie_speed

	outputfile.write("CASE #" + str(i+1) + ": " + "%.6f" %annie_speed + "\n")
