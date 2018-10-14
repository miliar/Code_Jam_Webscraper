import math

PI = 3.141592653589793238
T = int(input())

for t in range(T):
    N, K = list(map(int, input().split()))
    p = []
    for i in range(N):
        p.append(list(map(int, input().split())))

    best_ans = 0
    for i in range(N):
        out = p[i]
        pp = p[:i]+p[i+1:]
        pp = sorted(pp, key=lambda q: q[0]*q[1], reverse=True)
        pp = pp[:K-1]
        pp.append(out)
        #print(pp)
        s = sum([2*PI * x[0] * x[1] for x in pp])
        ans = PI * (out[0]**2) + s
        best_ans = max(ans, best_ans)
        #print(ans)
    print('Case #{0:d}: {1:.10f}'.format(t+1, best_ans))
