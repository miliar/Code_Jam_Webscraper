import sys, math

sys.setrecursionlimit(2500)

from collections import Counter

inp = open("in.txt")
#out = sys.stdout
out = open("out.txt","w+")

IMP = "IMPOSSIBLE"

def print_case(case, result):
    debug("Case #%d: %s" % (case, str(result)))
    out.write("Case #%d: %s\n" % (case, str(result)))

def debug(message):
	if len(sys.argv) > 1 and sys.argv[1] == "silent":
		return
	sys.stdout = sys.__stdout__
	print message
	sys.stdout = out

def read_ints(f=False):
    g =float if f else int
    return [g(x) for x in inp.readline().split()]

flatten = lambda l: [item for sublist in l for item in sublist]

T = int(inp.readline())
for t in xrange(T):
    n, r, o, y, g, b, v = read_ints()
    m = max([r,o,y,g,b,v])
    a = sorted([(r, "R"), (y, "Y"), (b, "B")], reverse=True)
    
    if (n / float(m)) < 2:
        print_case(t+1, IMP)
        continue
    
    q = [a[0][1]] * a[0][0]
    a = a[1:]
    l = len(q)
    j = 0
    while len(a) != 0:
        for i in xrange(a[0][0]):
            q[j] += a[0][1]
            j = (j + 1) % l
        a = a[1:]
    
    print_case(t+1, "".join(flatten(q)))
    
