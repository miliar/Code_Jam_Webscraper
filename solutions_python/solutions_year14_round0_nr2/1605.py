import sys

def getOptTime(c, f, target):
	if target <= 0:
		return 0
	numCookies = 0
	rate = 2
	t = 0 # time
	
	# first check if buying farm *possible*, then check if *feasible*
	#(Non sequitur: buying the farm is a rather morbid turn of phrase)
	while numCookies < target: 
		if ((target - numCookies) > c):# then run till you have c cookies
			t += c / rate # 15+7.5+5
			numCookies += c
			if ((target - numCookies) / rate) > (((target-numCookies)+c)/(rate+f)):
				numCookies -= c
				rate += f # 4, 6
			else:
				t += (target - numCookies)/rate # + 11.666666667
				numCookies = target			
		else:
			t += (target - numCookies)/rate
			numCookies = target		
	return t	# 39.166666x
	
	
def getInp(fyle):
	fh = open(fyle)
	numCases = int(fh.readline())
	for i in range(numCases):
		l = [float(x) for x in fh.readline().split()]
		c, f, x = l[0], l[1], l[2]
		tyme = getOptTime(c, f, x)
		print 'Case #%s: %.7f' %(i+1, tyme)
		

if len(sys.argv) != 2:
	print "Here's the format: <thisfilename.py> <inputstuff>  , Try again."
else:
	phile = sys.argv[1]
	getInp(phile)
