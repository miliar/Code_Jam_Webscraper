#!/usr/python
#read in file
#Iterate over each line
#  smax = the first value
#  roster = the second value
roster = []
num_tests = 0

with open("A-large.in") as f:
	num_tests = int(f.readline())
	for line in f:
		test = line.strip().split()
        	roster.append(test)


##
#For testing purposes
##

#roster = ["11111", "09", "110011", "1"]

f = open('audienceOutput.txt', 'w+')
###END TEST##

for test in range(0, num_tests):
	audience_standing = 0
	friends_needed = 0
	for i in range(0,len(roster[test][1])):
		#print "audience standing :: " + str(audience_standing) 
		#print "current shyness :: " + str(i)
		#print "audience count with shyness :: " + roster[test][i]
		if(audience_standing < i):
			#print "THESE PEOPLE ARE TOO SHY TO STAND WITH THE CURRENT NUMBER OF POEPLE STANDING"
			friends_needed += i-audience_standing
			audience_standing += i-audience_standing
		#print (roster[test][1])
		audience_standing += int(roster[test][1][i])

	f.write("Case #" + str(test+1)+": " + str(friends_needed) + " \n")	
	#print "Friends Needed : " + str(friends_needed)


#print output to file



