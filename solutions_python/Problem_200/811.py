# Problem B. Tidy Numbers

import os

SOURCE = '%s/../Resources/Q2Al.in' % os.path.dirname(__file__)
TARGET = '%s/../Resources/Q2Al.out' % os.path.dirname(__file__)

INPUT = open(SOURCE).read().splitlines()
OUTPUT = open(TARGET, 'w')


def change(A, i):
    if i < 0:
        A[:] = [9] * (len(A) - 1)
        return

    if A[i] == 1:
        change(A, i - 1)

    else:
        A[i] -= 1

        if i > 0 and A[i-1] > A[i]:
            change(A, i-1)

        else:
            for j in xrange(i+1, len(A)):
                A[j] = 9

T = int(INPUT.pop(0))
for t0 in xrange(T):
    OUTPUT.write('Case #%d: ' % (t0 + 1))
    print 'Case #%d: ' % (t0 + 1)

    N = map(int, INPUT.pop(0))
    print ''.join(map(str, N))

    p = 0
    for idx, c in enumerate(N):
        if c < p:
            change(N, idx-1)
            break

        p = c

    print ''.join(map(str, N))
    OUTPUT.write('%s\n' % ''.join(map(str, N)))
