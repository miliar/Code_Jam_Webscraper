T = int(raw_input())

for t in range(1, T+1):
    D, N = map(int, raw_input().split())
    K = [0] * N
    S = [0] * N
    mx = 0.0
    for i in range(N):
        K[i], S[i] = map(int, raw_input().split())
        mx = max(mx, (D - K[i])*1.0/S[i])
    
    print 'Case #%d: %f' % (t, D / mx)
    