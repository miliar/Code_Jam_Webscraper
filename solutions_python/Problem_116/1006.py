import numpy as np, sys

def proc(case):
    a = np.array(map(list, case))
    #print a

    for i in range(4):
        r = a[i,:]
        if ((r == 'X') | (r == 'T')).all():
            return 'X won'
        if ((r == 'O') | (r == 'T')).all():
            return 'O won'
        r = a[:,i]
        if ((r == 'X') | (r == 'T')).all():
            return 'X won'
        if ((r == 'O') | (r == 'T')).all():
            return 'O won'

    d = a[range(4), range(4)]
    if ((d == 'X') | (d == 'T')).all():
        return 'X won'
    if ((d == 'O') | (d == 'T')).all():
        return 'O won'
    d = a[range(4), range(3,-1,-1)]
    if ((d == 'X') | (d == 'T')).all():
        return 'X won'
    if ((d == 'O') | (d == 'T')).all():
        return 'O won'

    if (a == '.').sum():
        return 'Game has not completed'

    return 'Draw'

with open(sys.argv[1]) as f:
    n = int(f.readline())

    for i in range(n):
        case = [f.readline().strip() for _ in range(4)]
        print 'Case #%d: %s' % (i+1, proc(case))

        f.readline()
