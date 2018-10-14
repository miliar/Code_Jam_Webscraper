import sys

num_cases = int(sys.stdin.readline())

def slowtest(a,b, c):
	a.sort()
	#print a, b
	v = a[len(a)-1]
	max_min = v + b
	if (b >= c):
		return max_min
	
	m = max_min
	d = a[:-1]
	if (v <= 1): 
		return max_min
	for i in xrange(1,(v/2)+1):
	
		t = slowtest(d + [i,v-i],b+1, c)
		if (t < max_min):
			max_min = t
	return max_min
	
def result(a):	
	minutes = 0
	a = a.split()
	diners = len(a)
	a = map(int,a)
	a.sort()
	##print a
	
	minutes = a[len(a)-1]
	return str(slowtest(a,0,minutes))

	



for i in range(1,num_cases+1):
	sys.stdin.readline()	
	print "Case #" + str(i) + ": " + result(sys.stdin.readline())
	#print "-----------"

