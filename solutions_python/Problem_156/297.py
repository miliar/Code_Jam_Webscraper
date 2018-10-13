data = open("B-large.in","r")
outfile = open("cj_pancakes_large.txt","w")

import math

t = int(data.readline())
for case in range(0,t):
	diners = int(data.readline())
	pancakes_temp = data.readline().split(' ')
	if case < t-1:
		pancakes_temp[-1]=pancakes_temp[-1][:-1] #get rid of the '\n'
	#print diners
	#print pancakes_temp
	pancakes = []
	for item in pancakes_temp:
		pancakes.append(int(item))
	#print pancakes
	
	#print "\n"
	
	max_pancakes = max(pancakes)
	optimum = max_pancakes
	for test_max in range(max_pancakes,0,-1):
		#try out different possible maxes
		moves = 0
		for value in pancakes:
			if value > test_max:
				moves+=math.ceil(float(value)/float(test_max))-1
		if test_max + moves <= optimum:
			#print "new optimum found: reduce to " + str(test_max)
			optimum = test_max + moves
			#print test_max
			#print moves
	outfile.write("Case #" + str(case+1) + ": " + str(int(optimum)))
	if case < t-1: outfile.write("\n")
	#print int(optimum)
	#print "\n"