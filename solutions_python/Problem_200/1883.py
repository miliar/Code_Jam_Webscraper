def getnum(l):
	# l is list of int
	l = [str(x) for x in l]
	i = int(("").join(l))
	return i

def posi(l):
	#return first index in list where increasing
	rval = 25 #greater than large input no of digits
	dl = [x>y for x,y in zip(l,l[1:])]
	try:
		rval = dl.index(True)
	except ValueError:
		#all val False ie list is nondecreasing
		rval = -1
	return rval

def changef(f,i):
	#since i is the pos such that f[i]>f[i+1], f[i] > 0 so below always valid
	f[i] = f[i] - 1
	if f[i] == -1:
		print "Whaaaaat?"
	

	for j in range(i+1,len(f)):
		f[j] = 9

	a = getnum(f)
	return a


def construct_tidy(n):
	#n is an int
	s = str(n)
	d = list(s)
	f = [int(x) for x in d]
	
	while posi(f) != -1:
		
		a = changef(f,posi(f))

		d = list(str(a))
		f = [int(x) for x in d]
	
	#list is non-decreasing now
	return getnum(f)
	
	

if __name__ == "__main__":

	t = int(raw_input())
	for i in range(1, t+1):
		n = int(raw_input())
		a = construct_tidy(n)	
		print "Case #" + str(i) + ": " + str(a)





