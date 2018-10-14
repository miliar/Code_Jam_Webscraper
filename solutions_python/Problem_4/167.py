import sys

sys.stdin = open('input', 'r')
sys.stdout = open('output', 'w')


for test in xrange(1, int(sys.stdin.readline()) + 1):
    dim = int(sys.stdin.readline())
    v1 = map(int, sys.stdin.readline().split(" "))
    v2 = map(int, sys.stdin.readline().split(" "))

    v1.sort()
    v2.sort()
    v2.reverse()
    prod = 0
    
    for i in xrange(dim):
        prod += v1[i]*v2[i]

    print "Case #%d: %s" % (test, prod)
