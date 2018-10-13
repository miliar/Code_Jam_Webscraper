import sys
import time
import math

with open(sys.argv[1]) as f:
	T  = int(f.readline())
	content = f.readlines()

#print "T is",T

def eat(motes, size,added):
	if len(motes) == 0:
		return motes,size,added
	if (size == 1):
		return eat(motes[:-1],size,added+1)

	#print "Eat:",motes,size,added

	last = motes[-1]
	if last < size:
		return eat(motes[:-1], size+motes[-1],added)
	else:
		m1,s1,a1 = eat(motes[:],size+size-1,added+1)
		m2,s2,a2 = eat(motes[:-1],size,added+1)
		if a1 < a2:
			return m1,s1,a1
		else:
			return m2,s2,a2

def neg(v):
	return -v

for t in range(T):
	param = [int(k) for k in content[t*2].split()]
	motes = sorted([int(k) for k in content[t*2+1].split()], key=neg)
	#nums = [int(k) for k in content.split()]
	start = param[0]
	size = start
	added = 0

	motes,size,added = eat(motes,size,added)

		
		#print start,motes,added
	#print "ANSWER:",added
	print "Case #%d: %d" % (t+1,added)