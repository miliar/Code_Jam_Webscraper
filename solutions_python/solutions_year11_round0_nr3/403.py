import sys

def process(l):
     l = map(int, l)
     if reduce(lambda x,y : x^y, l) != 0:
         return "NO"
     return sum(l)-min(l)

T = int(sys.stdin.readline().strip())
for i in xrange(T):
    sys.stdin.readline()
    print "Case #%d:"%(i+1), process(sys.stdin.readline().strip().split(" "))

