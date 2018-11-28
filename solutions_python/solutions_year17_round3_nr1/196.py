from math import pi
T = int(raw_input())
for t in range(1, T+1):
    N, K = map(int, raw_input().split())
    R = []
    H = []
    C = []
    for n in range(N):
        r, h = map(float, raw_input().split())
        R.append(r)
        H.append(h)
        C.append((r, h))
    #C_max = max(C, lambda x: x[0]**2 + 2*x[0]*x[1])
    #i_max = C.index(C_max)
    #C = [C[i] for i in range(len(C)) if i != i_max]
    max_ans = 0
    C = sorted(C, key=lambda x: x[0], reverse=True)
    for i in range(N-K+1):
        C2 = [C[i]] + sorted(C[i+1:], key=lambda x:2*x[0]*x[1], reverse=True)[:K-1]
        ans = pi*(C2[0][0])**2
        ans += 2*pi*sum([c[0]*c[1] for c in C2])
        max_ans = max(ans, max_ans)
    print 'Case #{}: {}'.format(t, max_ans)


