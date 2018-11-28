import sys

def process(l):
    return l[0]

T = int(sys.stdin.readline().strip())
for i in xrange(T):
    print "Case #%d:"%(i+1), process(sys.stdin.readline().strip().split(" "))

