#!/usr/bin/python
import math
def gcd(a, b):
	if b==0:
		return a
	else:
		return gcd(b, a%b)
	
filename = map(str.rstrip, open("B-small.in", 'r').readlines())
output = open("B-small.out", 'w')
c = int(filename[0])
for x in xrange(c):
        b = filename[x+1].split(' ')
        n = int(b[0])
        lists = [int(d) for d in b[1:]]
        lists.sort()
	lists.reverse()
        diffs = [lists[d] - lists[d+1] for d in xrange(len(lists)-1)]
	diffs.sort()
	counter = -1
	cur = diffs[0]
	while diffs[0] != diffs[counter]:
		cur = gcd(cur, diffs[counter])
		counter = counter-1
	w = math.ceil(float(min(lists))/float(cur))
	print w
	print >>output, "Case #"+str(x+1) + ":", int((cur*w)-min(lists))

output.close()
