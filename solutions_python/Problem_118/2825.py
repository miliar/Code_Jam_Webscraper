import math
import string
infile = file("C-small-attempt0.in")
linebuff = infile.readline()
caseamount = string.atoi(linebuff)

def isFair( strIn ):
	if type(strIn)==type(1):
		strIn = str(strIn)
	if int(strIn) <=0:
		return False
	leng = len(strIn)
	for i in xrange(leng/2):
		if strIn[i] != strIn[leng - i-1]:
			return False
	return True

# for x in xrange(2000):
	# print x, "is",
	# if not isFair(str(x)):
		# print "NOT",
	# print "fair."
	# if isFair(str(x)):
		# print x
		
	
for cases in xrange(caseamount):
	linebuff = infile.readline()
	lowerlimit = int(linebuff.split()[0])
	upperlimit = int(linebuff.split()[1])
	upper = int(math.sqrt(upperlimit))
	lower = int(math.sqrt(lowerlimit) + 0.9999999)
	#print lower, upper
	total = 0
	# generate square root
	for x in xrange(lower, upper+1):
		if isFair(x):
			if isFair(x*x):
				total+= 1
	print "Case #"+str(cases+1)+": "+str(total)
	#Case #1: 2
	
	
	
	# if result == '.':
		# print "Case #"+str(cases+1)+": Game has not completed"
	# if result == 'D':
		# print "Case #"+str(cases+1)+": Draw"
	# elif result == 'X' or result == 'O':
		# print "Case #"+str(cases+1)+": "+str(result)+" won"
	
	