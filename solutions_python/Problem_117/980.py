import numpy as np, sys

def proc(case):
    a = np.array(map(list, case))
    #print a

    while True:
        if 1 in a.shape: return True

        x, y = np.unravel_index(a.argmin(), a.shape)
        m = a[x,y]

        #print x, y

        if (a[x,:] == m).all():
            a = np.delete(a, x, 0)
        elif (a[:,y] == m).all():
            a = np.delete(a, y, 1)
        else:
            return False

with open(sys.argv[1]) as f:
    t = int(f.readline())

    for i in range(t):
        n, m = map(int, f.readline().split())
        case = [map(int, f.readline().split()) for _ in range(n)]
        print 'Case #%d: %s' % (i+1, ['NO', 'YES'][proc(case)])
