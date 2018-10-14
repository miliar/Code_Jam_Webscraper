import sys
import psyco
from operator import xor
psyco.full()
def dbg(a): sys.stderr.write(str(a))
def readarray(foo): return [foo(x) for x in raw_input().split()]

def run_test():
	n = int(raw_input())
	a = readarray(int)
	if reduce(xor, a): return "NO"
	return str(sum(a) - min(a))

for test in range(int(raw_input())):
	dbg("Test %d\n" % (test + 1))
	print "Case #%d: %s" % (test + 1, run_test())
