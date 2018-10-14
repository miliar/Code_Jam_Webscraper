import sys
import psyco
from operator import xor
psyco.full()
def dbg(a): sys.stderr.write(str(a))
def readarray(foo): return [foo(x) for x in raw_input().split()]

def run_test():
	n = int(raw_input())
	p = readarray(int)
	res = len(filter(lambda x: x[0] != x[1] - 1, enumerate(p)))
	return "%.5f" % res

for test in range(int(raw_input())):
	dbg("Test %d\n" % (test + 1))
	print "Case #%d: %s" % (test + 1, run_test())
