from sys import stdin
from collections import defaultdict
import math

def palgen(fr,to):
	# n=1
	# prefix_len = (len(str(fr)+1)/2
	# start = str(fr)

	st=str(int(math.sqrt(fr)))
	n=int(st[:(len(st)+1)/2])

	# print st, n, "*"

	yy=0
	odd=True
	nasstr=str(n)
	while yy*yy<=to:
		rangestart = -2 if odd else -1

		# print str(n) + " " + str(n)[rangestart::-1]
		yy=int(nasstr + nasstr[rangestart::-1])
		# print ">>", yy, str(n), str(n)[rangestart::-1]
		yield yy
		# yield int(str(n) + str(n)[0::-1])
		(oldnasstr, n) = nasstr, n+1
		nasstr=str(n)
		if len(oldnasstr)<len(nasstr):
			if odd:
				n=n/10
				nasstr=str(n)
			odd = not odd
			# print "switch: " + str(rangestart), odd
		# n+=1

def is_palindrome(candidate):
	s = str(candidate)
	preflen=len(s)/2
	prefix=s[:preflen]
	endreversed=s[-1:-preflen-1:-1]
	return prefix==endreversed

# for v in palgen(120,10000):
# 	if is_palindrome(v*v):
		# print v, v*	v
		# pass

for cs in xrange(1,1+int(stdin.readline().strip())):
	(a,b) = [int(z) for z in stdin.readline().strip().split()]
	# print a,b
	sol=0
	for v in palgen(a,b):
		sq = v*v
		if sq >=a and sq <=b and is_palindrome(sq):
			sol+=1
	print "Case #" + str(cs) + ": " + str(sol)




