import sys
import psyco
psyco.full()
def dbg(a): sys.stderr.write(str(a))
def readint(): return int(raw_input())
def readfloat(): return float(raw_input())
def readarray(foo): return [foo(x) for x in raw_input().split()]


def run_test(test):
	dbg("Test %d\n" % (test + 1))
	(n, k) = readarray(int)
	res = (((1 << n) - 1) | k) == k
	print "Case #%d: %s" % (test + 1, "ON" if res else "OFF")

for test in range(readint()):
	run_test(test)

