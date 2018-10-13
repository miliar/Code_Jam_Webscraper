from sys import argv

f = open(argv[1])
def readint(): return int(f.readline())
def readarray(): return [int(x) for x in f.readline().split()]


for t in xrange(readint()):
    N = readint()

    A = {}
    for i in xrange(N):
        a, b = readarray()
        A[a] = b

    r = 0
    for a, b in A.items():
        for v, w in A.items():
            if a < v and b > w: r += 1
            if a > v and b < w: r += 1

    print "Case #%d: %d" % (t+1, r/2)

