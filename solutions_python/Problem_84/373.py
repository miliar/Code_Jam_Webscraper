import array

f = open('a-large.in','r')
o = open('a-large.out','w')

T = int(f.readline())

for t in xrange(T):
    o.write('Case #' + str(t+1) + ':\n')

    R,C = [int(x) for x in f.readline().split()]

    P = []

    for i in xrange(R):
        P.append(array.array('c', f.readline()))

    psbl = True

    for i in xrange(R-1):
        for j in xrange(C-1):
            if P[i][j] == '#':
                if P[i+1][j] == '#' and P[i+1][j+1] == '#' and P[i][j+1] == '#':
                    P[i][j]     = '/'
                    P[i+1][j]   = '\\'
                    P[i+1][j+1] = '/'
                    P[i][j+1]   = '\\'
                else :
                    psbl  = False
                    break
    
    if psbl:
        for i in xrange(R):
            if P[i][C-1] == '#':
                psbl = False
                break
        for i in xrange(C):
            if P[R-1][i] == '#':
                psbl = False
                break

    if psbl:
        for i in xrange(R):
            for j in xrange(C):
                o.write(P[i][j])
            o.write('\n')
    else :
        o.write('Impossible\n')

