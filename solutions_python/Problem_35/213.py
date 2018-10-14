#!/usr/bin/python

CHARS = [ord('A')+c for c in range(26)]

def sinks(c, n, w, e, s):
    if c <= min(n, w, e, s):
        return 0
    if n == min(n, w, e, s):
        return -1
    if w == min(n, w, e, s):
        return -2
    if e == min(n, w, e, s):
        return -3
    if s == min(n, w, e, s):
        return -4
          
def solve(M, H, W):
    A = [list(M[i]) for i in range(H+1)]
    for i in range(H):
        for j in range(W):
            A[i][j] = sinks(M[i][j], M[i-1][j], M[i][j-1], M[i][j+1], M[i+1][j])

    k = 0
    for i in range(H):
        for j in range(W):
            if A[i][j] == 0:
                A[i][j] = CHARS[k]
                k = k +1

    has_work = 1
    while has_work:
        has_work = 0
        for i in range(H):
            for j in range(W):
                if A[i][j] < 0:
                    s = (A[i-1][j], A[i][j-1], A[i][j+1], A[i+1][j])[-1-A[i][j]]
                    if s in CHARS:
                        A[i][j] = s
                    else:
                        has_work = 1
    R = ''
    for i in range(H):
        for j in range(W):
            R = R + chr(A[i][j])
            if j <= W-2:
                R = R + ' '
        if i < H-1:
            R = R + '\n'

    k = 0
    for i in range(len(R)):
        if ord(R[i]) in CHARS:
            R = R.replace(R[i], chr(ord('a') + k))
            k = k+1

    return R

if __name__ == '__main__':
    import sys
    inp = open(sys.argv[1], "r")
    T = int(inp.readline())
    for k in range(T):
        (H, W) = inp.readline().split(' ')
        (H, W) = (int(H), int(W))
        M = []
        for i in range(H):
            M.append(map(lambda x: int(x), inp.readline().split(' ')) + [float('infinity')])
        M.append([float('infinity') for i in range(W+1)])
        if (H >= 1) and (W >= 1):
            print 'Case #%d:' % (k+1)
            print solve(M, H, W)
