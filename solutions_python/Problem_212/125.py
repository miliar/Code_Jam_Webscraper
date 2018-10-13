def solve(N, P, G):
    C = [0]*P
    for g in G:
        C[g%P] += 1
    ans = C[0]
    C[0] = 0
    if P==2:
        pass
    elif P==3:
        c = min(C[1], C[2])
        ans += c
        C[1] -= c
        C[2] -= c
    elif P==4:
        c = min(C[1], C[3])
        ans += c
        C[1] -= c
        C[3] -= c
        c = C[2]/2
        ans += c
        C[2] -= c*2
    for i in range(P):
        c = C[i]/P
        ans += c
        C[i] -= c*P
    if sum(C)>0:
        ans += 1
    return ans

T = input()
for t in range(T):
    N,P = map(int, raw_input().split())
    G = map(int, raw_input().split())
    ans = solve(N, P, G)
    print "Case #%d: %d" % (t+1, ans)
