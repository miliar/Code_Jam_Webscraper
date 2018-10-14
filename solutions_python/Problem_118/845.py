
import math
import bisect
MAX = 10**14
SQR_MAX = 10**7
tab = []

def is_fair(a):
	a = str(a)
	for i in xrange(len(a) / 2):
		if a[i] != a[len(a) - i - 1]:
			return False
	return True

c=0
i=0
while c<MAX:
	c = i*i
	if is_fair(c) and is_fair(i):
		tab.append(c)
	i += 1


runs = input()
#runs = 10000

for run in xrange(runs):
	A,B = [ int(x) for x in raw_input().split() ]
	#A,B = 0, 10000
	x = bisect.bisect_left(tab, A)
	y = bisect.bisect_right(tab, B)
	#print tab[x:y]
	print "Case #%d: %s" % (run+1, y-x)
		
	

