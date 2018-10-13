from sys import stdin

T = int(stdin.readline())
for t in range(1, T + 1):
    N = int(stdin.readline())
    M = [int(s) for s in stdin.readline().strip().split()]
    a, r, b = 0, 0, 0
    for i in range(1,N):
        eaten = max(0, M[i-1] - M[i])
        a += eaten
        r = max(r, eaten)
    for i in range(1,N):
        b += min(r, M[i-1])
    print("Case #%s: %s %s" % (t, a, b))
