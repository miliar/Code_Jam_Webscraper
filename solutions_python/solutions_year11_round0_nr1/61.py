import sys
import psyco
psyco.full()
def dbg(a): sys.stderr.write(str(a))
def readarray(foo): return [foo(x) for x in raw_input().split()]

def run_test():
	pos = [1, 1]
	last = [0, 0]
	time = 0
	a = readarray(str)
	for i in xrange(int(a[0])):
		r, p = a[2 * i + 1] == 'O', int(a[2 * i + 2])
		time = max(time, abs(p - pos[r]) + last[r]) + 1
		pos[r], last[r] = p, time		
	return str(time)

for test in range(int(raw_input())):
	dbg("Test %d\n" % (test + 1))
	print "Case #%d: %s" % (test + 1, run_test())
