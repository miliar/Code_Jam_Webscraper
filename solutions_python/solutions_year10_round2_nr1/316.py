import sys

getln = lambda: sys.stdin.readline()

def solve():
    root = {}
    cc = 0
    ec, nc = map(int, getln().split())
    getPath = lambda: getln()[1:-1].split("/")

    def create(path):
        c = 0
        p = root
        for d in path:
            if d not in p:
                p[d] = {}
                c += 1
            p = p[d]
        return c

    for x in xrange(ec):
        create(getPath())
    for x in xrange(nc):

        cc += create(getPath())
    return cc

for case in xrange(int(getln())):
    print "Case #%s: %s" % (case + 1, solve())
