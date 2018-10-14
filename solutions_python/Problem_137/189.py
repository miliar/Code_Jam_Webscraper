
import sys
in_ = sys.stdin

def find(R, C, M):
    in_1 = lambda i, j: (i >= R - sy_1 and j >= C - sx_1)
    in_2 = lambda i, j: (i >= R - sy_2 and j >= C - sx_2)
    check = lambda i, j: not (in_1(i, j) or in_2(i, j))
    for sx_1 in xrange(2, C + 1):
        for sy_1 in xrange(2, R + 1):
            for sx_2 in xrange(sx_1, C + 1):
                for sy_2 in xrange(2, sy_1 + 1):
                    size = sx_1 * sy_1 + sx_2 * sy_2
                    size -= min(sx_1, sx_2) * min(sy_1, sy_2)
                    if R * C - size == M:
                        return [[('*' if check(i, j) else '.')
                                 for j in xrange(C)] for i in xrange(R)]

T = int(in_.readline())
for t in xrange(T):
    R, C, M = map(int, in_.readline().split(' '))
    A = [['.'] * C for i in xrange(R)]
    print 'Case #%d:' % (t + 1)

    if M >= R * C - 1:
        A = [['*'] * C for i in xrange(R)] \
            if M < R * C else None
    elif R == 1:
        A = [['*'] * M + ['.'] * (C - M)]
    elif C == 1:
        A = [['*' if i < M else '.'] for i in xrange(R)]
    elif M <= (R - 2) * (C - 2):
        r = M
        for i in xrange(R - 2):
            x = min(r, C - 2)
            r = max(r - x, 0)
            A[i] = ['*'] * x + ['.'] * (C - x)
    else:
        A = find(R, C, M)

    if A is not None:
        A[-1][-1] = 'c'
        for line in A:
            print ''.join(line)
    else:
        print 'Impossible'
