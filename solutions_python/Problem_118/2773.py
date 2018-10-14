import math

f = open('testinput.in', 'r')
numcases = long(f.readline())
#print numcases
#print "Number of Cases: "+str(numcases)
for i in range(numcases):
	ar = f.readline()
	z = ar.split()
	x = long(z[0])
	y = long(z[1])
	pals = []
	splitted = []
	total = []
	for j in range(x,y+1):
		if(str(j) == str(j)[::-1]):
			pals.append(j)
	#print pals
	for j in range(len(pals)):
		sqrted = math.sqrt(pals[j])
		if(long(str(sqrted).split(".")[1]) == 0):
			splitted.append(str(sqrted).split(".")[0])
	for j in range(len(splitted)):
		if splitted[j] == splitted[j][::-1]:
			total.append(splitted[j])
	print "Case #"+str(i+1)+": "+str(len(total))