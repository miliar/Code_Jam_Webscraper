
import sys
from decimal import Decimal
import multiprocessing

def isPal(x):
	s = str(x)
	for a, b in zip(s, reversed(s)):
		if a != b: return False
	return True


def createCache(x, xfin, conn):
	#y = x*x
	r = []
	#print >>sys.stderr, (x, xfin, r)
	while x <= xfin:
		if isPal(x):
			y = x*x
			if isPal(y): r.append(y)
		x += 1
        	#y += x
		#x += 1
		#y += x
	conn.send(r)
	conn.close()



parent_conn1, child_conn1 = multiprocessing.Pipe()
t1 = multiprocessing.Process(target=createCache, args=(long(1), long('1' + '0'*6), child_conn1))
t1.start()


parent_conn2, child_conn2 = multiprocessing.Pipe()
t2 = multiprocessing.Process(target=createCache, args=(long('1' + '0'*6) +1, long('1' + '0'*7), child_conn2))
t2.start()

t1.join()
t2.join()
cache = parent_conn1.recv() + parent_conn2.recv()
#print c1
#print c2
#print cache
#createCache(long(1), long('1' + '0'*7), cache)

cases = input()
for c in xrange(cases):
	xin, xfin = raw_input().split()

	xin = long(xin)
	xfin = long(xfin)
	
	sys.stdout.write('Case #%d: ' % (c+1))
	print sum( xin <= e <= xfin for e in cache )

