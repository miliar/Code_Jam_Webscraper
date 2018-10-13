#! /usr/bin/python

inpfile = open('small1.in','r')

inpCount = int (inpfile.readline())
ind = 0
case = 0

while ind < inpCount:
	vectorCount = int(inpfile.readline())
	a = 0
	temp1 = []
	t1 = inpfile.readline()
	temp0 = t1.strip("\n").split(" ")
	temp1 = []
	for i in temp0:
		temp1.append(int(i))
	temp1 = sorted(temp1)
	#print temp1
	t2 = inpfile.readline()
	temp3 = t2.strip("\n")
	temp3 = temp3.split(" ")
	temp2 = []
	for i in temp3:
		temp2.append(int(i))

	temp2 = sorted(temp2)
	#print temp2 

	count = 0
	sum = 0
	while count < len(temp2):
		#print int(temp1[count])*int(temp2[len(temp1)-count-1])
		sum = sum + int(temp1[count])*int(temp2[len(temp1)-count-1])
		count = count + 1
	
	case = ind + 1
	print "Case #%d: %d" % (case, sum)
	ind = ind + 1

