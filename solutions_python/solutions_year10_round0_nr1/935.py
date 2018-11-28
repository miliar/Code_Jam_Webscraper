import sys
from copy import copy

fd = open(sys.argv[1])

def get_line(fd):
    return fd.readline().replace('\n', '')

cases = int(get_line(fd))+1

states = {True: 'OFF', False: 'ON'}

for case in xrange(1, cases):
    N, K = map(int, get_line(fd).split(' '))

    snappers = [0] * N

    for k in xrange(K):
        last = 0
        org_snappers = copy(snappers)

        for i, v in enumerate(snappers):
            if i !=0 and org_snappers[i-1] == 0:
                break
            if org_snappers[i] == 1:
                snappers[i] = 0
            else:
                snappers[i] = 1

    answ = states[0 in snappers]

    print 'Case #%s: %s' % (case, answ)

