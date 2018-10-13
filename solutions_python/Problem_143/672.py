T = int(raw_input())

def nwins(A, B, K):
    s = 0
    for a in range(A):
        for b in range(B):
            if a & b < K:
                s += 1
    return s
for i in range(T):
    A, B, K = map(int, raw_input().split())
    print 'Case #%d: %d' % (i + 1, nwins(A, B, K))
