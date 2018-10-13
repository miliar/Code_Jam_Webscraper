import sys
import time

inputfile = open(sys.argv[1],'r')
outputfile = open(sys.argv[1].replace("in","out"),'w')

testcases = int(inputfile.readline())

for i in range(0, testcases):
	number_str = inputfile.readline().strip()

	for index in reversed(range(len(number_str))):
		print number_str
		print index
		if index != 0:
			if number_str[index] < number_str[index-1]:
				print str(index) + " " + number_str[index] + " " + number_str[index-1]
				index_num = int(number_str[index-1]) - 1
				print "DEBUG: " + str(len(number_str)) + " " + str(index)
				nines = '9' * (len(number_str)-index) 
				#print nines
				number_str = number_str[:index-1] + str(index_num) + nines
				#print "NUMBER: " + number_str

	outputfile.write("CASE #" + str(i+1) + ": " + str(int(number_str)) + "\n")

outputfile.close()
