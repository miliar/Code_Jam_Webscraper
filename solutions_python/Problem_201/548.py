import sys

def solve(N,K):
    T = {N:1}
    depth = 0
    while 2**depth < K:
        TT = {}
        for n, cnt in T.items():
            if n % 2 == 0:
                TT[n//2] = TT.get(n//2,0) + cnt
                TT[n//2-1] = TT.get(n//2-1,0) + cnt
            else:
                TT[n//2] = TT.get(n//2,0) + 2*cnt
        K -= 2**depth
        depth += 1
        T = TT
    T = sorted(T.items(), reverse=True)
    while T[0][1] < K:
        K -= T[0][1]
        T.pop(0)
    n = T[0][0]
    if n % 2 == 0:
        return n//2,n//2-1
    return n//2,n//2

for t in range(1,int(input())+1):
    N,K = map(int,sys.stdin.readline().split())
    ma,mi = solve(N,K)
    print("Case #{}: {} {}".format(t,ma,mi))
