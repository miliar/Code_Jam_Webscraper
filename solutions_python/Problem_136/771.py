#!/usr/bin/env python

import sys
import re

total_tests = 0
basic_production = 2.0
ctr = 0
time = 0.0
timeList = []

for line in sys.stdin:
	if ctr == 0:
		total_tests = int(line)
	else:
		arguments =  re.findall("\d+.\d+", line)
		farm_price = float(arguments[0])
		farm_production = float(arguments[1])
		goal = float(arguments[2])

		while True:
			if (goal/basic_production) <= ((goal/(basic_production+farm_production))+(farm_price/basic_production)):
				time = goal/basic_production
				break
			else:
				time = 0	
				timeList.append(farm_price/basic_production)
				basic_production = basic_production + farm_production
		for num in timeList:
			time = time + num
	
		sys.stdout.write("Case #" + str(ctr) +": ")
		sys.stdout.write('%1.7f' % time)
		sys.stdout.write('\n')
		timeList = []
		time = 0
		basic_production = 2.0
	ctr = ctr + 1

