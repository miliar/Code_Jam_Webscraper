
def solve():
    D, N = map(int, raw_input().split())
    horses = []
    for i in range(N):
        K, S = map(int, raw_input().split())
        horses.append((K,S))
    t = lambda (k,s): float((D-k))/s
    last = max(horses, key=t)
    tt = t(last)
    return float(D)/tt



T = int(raw_input())
for t in range(1, T+1):
    print "Case #{}: {}".format(t, solve())
