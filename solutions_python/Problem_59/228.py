import sys
import psyco
psyco.full()

cases = int(sys.stdin.readline().strip())
for case in xrange(1, cases + 1):
    n, m = map(int, sys.stdin.readline().strip().split(' '))
    dirs = ['/']
    for i in xrange(n):
        dae = sys.stdin.readline().strip().split('/')[1:]
        for j in xrange(1, len(dae) + 1):
            k = '/' + '/'.join(dae[:j])
            if k in dirs:
                continue
            dirs.append(k)
    mkdirs = 0
    for i in xrange(m):
        dtc = sys.stdin.readline().strip().split('/')[1:]
        for j in xrange(1, len(dtc) + 1):
            k = '/' + '/'.join(dtc[:j])
            if k in dirs:
                continue
            else:
                dirs.append(k)
                mkdirs += 1
    print 'Case #%d: %d' % (case, mkdirs)