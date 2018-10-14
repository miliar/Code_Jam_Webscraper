T = int(input())

for c in range(T):
    D,N = map(int,input().split())
    t = []
    for h in range(N):
        K,S = map(int,input().split())
        t.append((D-K)/S)
    ans = D / max(t)
    print('Case #',(c+1),': ',ans,sep='')
