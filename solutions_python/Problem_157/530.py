import math

V = [[1, 2, 3, 4], [2, -1, 4, -3], [3, -4, -1, 2], [4, 3, -2, -1]]
M = {'i':2, 'j':3, 'k': 4}
def comp(I):
    A = M[I[0]]
    S = 0
    for s in I[1:]:
        A = V[A-1][M[s]-1]
        if A < 0:
            A = -A
            S = S + 1
    if S % 2 == 0:
        return A
    else:
        return -A
def judge(I, N):
    for ii in range(1, N):
        if (comp(I[0:ii]) == M['i'] and comp(I[ii:])== M['i']):
            for jj in range(ii+1, N):
                if (comp(I[ii:jj]) == M['j']):
                        if (comp(I[jj:N]) == M['k']):
                            return 'YES'
    return 'NO'


for i in xrange(input()):
    line = raw_input()
    [N, R] = map(int, line.split())
    line = raw_input()
    I = line * R
    if (comp(I) != -1):
        print "Case #%d: %s" % (i + 1, 'NO')
    elif (len(set(I)) == 1):
        print "Case #%d: %s" % (i + 1, 'NO')
    else:
        print "Case #%d: %s" % (i + 1, judge(I, N * R))
