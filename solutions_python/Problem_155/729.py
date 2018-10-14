
import sys

def debug(args):
    print >> sys.stderr, args

fin = sys.stdin
T = int(fin.readline())
for case in range(1, T + 1):
    win = False
    a, b = fin.readline().split()
    smax = int(a)
    s = map(int, b)
    count = 0
    add = 0
    for i, n in enumerate(s):
    	if n > 0:
    		if i > count:
    			k = i - count
    			count += k
    			add += k
    		count += n

    print "Case #%d: %s" % (case, add)