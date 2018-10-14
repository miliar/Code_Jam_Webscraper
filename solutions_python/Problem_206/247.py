def solve():
    D,N = [int(v) for v in input().split()]
    h = []
    for i in range(N):
        ki,si = [int(v) for v in input().split()]
        h.append([ki,si])
    t = max((D-p[0])/p[1] for p in h)
    return D/t

T = int(input())
for t in range(1, T + 1):
    print('Case #%d: %.7f' % (t,solve()))


