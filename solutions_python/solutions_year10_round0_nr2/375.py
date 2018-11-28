from sys import stdin
from pprint import pprint
from fractions import gcd
readline = stdin.readline

T = int(readline())

for case in range(T):
	sss = map(int,readline().split(' ')[1:])
	smallest = min(sss)
	reindexedsss = map(lambda x:x-smallest,sss)
	g = reduce(gcd,reindexedsss)
	print "Case #%d: %d" % (case+1, (g-smallest%g)%g)
