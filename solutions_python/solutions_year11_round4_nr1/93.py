T = int(raw_input())
for test_case in range(1, T+1):
    data = map(int, raw_input().split())
    X = data[0]
    S = data[1]
    R = data[2]
    t = data[3]
    N = data[4]
    boost = R-S
    table = [0]*101
    table[0] = X
    for i in range(N):
        data = map(int, raw_input().split())
        Bi = data[0]
        Ei = data[1]
        wi = data[2]
        table[wi] += (Ei-Bi)
        table[0] -= (Ei-Bi)
    ans = 0.0
    done = False
    for i in range(101):
        if done:
            ans += (1.0*table[i])/(i+S)
        else:
            tx = (1.0*table[i])/(i+R)
            if t >= tx:
                ans += tx
                t -= tx
            else:
                done = True
                d1 = 1.0*(i+R)*t
                d2 = table[i] - d1
                ans += t + 1.0*d2/(i+S)
                t = 0
    print 'Case #%d: %.9f' % (test_case, ans)
    