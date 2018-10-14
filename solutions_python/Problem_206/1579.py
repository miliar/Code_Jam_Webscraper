T = int(input())
for i in range(T):
    D, N = map(int, input().split())
    maxt = 0
    for j in range(N):
        Ki, Si = map(int, input().split())
        ti = (D - Ki) / Si
        maxt = max(maxt, ti)
    print('Case #%d: %s' % (i+1, D / maxt))
