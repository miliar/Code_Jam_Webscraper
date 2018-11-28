import numpy as np
import sys

FILE_NAME = 'large'
f = open(FILE_NAME + '.in', 'r')
g = open(FILE_NAME + '.out', 'w')
# g = sys.stdout

T = int(f.readline())
for t in range(1, T + 1):

    # input# {{{
    D, N = [int(s) for s in f.readline().splitlines()[0].split(' ')]

    A = []
    for i in range(N):
        A += [int(s) for s in f.readline().splitlines()[0].split(' ')]
    A = np.array(A).reshape(N, 2)
    # }}}

    # calc# {{{
    B = (D - A[:,0]) / A[:,1]
    ans = D / np.max(B)
    # }}}

    # print# {{{
    print("Case #{}: {}".format(t, ans), file=g)
    # print("Case #{}: {} {}".format(t, P, Q), file=g)
    # for i in range(A.size):
        # if i != 0:
            # print(' ', end='', file=g)
        # print(A[i], end='', file=g)
    # print('', file=g)
    # }}}
