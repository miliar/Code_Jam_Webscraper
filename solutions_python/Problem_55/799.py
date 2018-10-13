import sys
from collections import deque

fd = open(sys.argv[1])

def get_line(fd):
    return fd.readline().replace('\n', '')

cases = int(get_line(fd))+1

def calc(R, groups, k):
    euro = 0
    glen = len(groups)

    for r in xrange(1, R):
        gsize = 0
        loop = 0
        while gsize < k:
            loop += 1
            if loop > glen:
                break
            groups.rotate(-1)
            gsize += groups[-1]
            if gsize > k:
                gsize -= groups[-1]
                groups.rotate()
                break

        euro += gsize
    return euro

for case in xrange(1, cases):
    R, k, n = map(int, get_line(fd).split(' '))
    groups =  deque(map(int, get_line(fd).split(' ')))

    euro = calc(R+1, groups, k)

    print 'Case #%s: %s' % (case, euro)

