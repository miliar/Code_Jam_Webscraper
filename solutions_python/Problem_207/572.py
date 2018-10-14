def solve():
    N,R,O,Y,G,B,V = [int(i) for i in raw_input().split()]
    # C = {'R': R, 'O': O, 'Y': Y, 'G': G, 'B': B, 'V': V}
    C = [['R',R],['Y',Y],['B',B]]

    C.sort(key=lambda x: x[1], reverse=True)
    sol = []
    sol.append(C[0][0])
    C[0][1]-=1

    for i in range(1,N):
        m = -1
        for j in range(len(C)):
            if C[j][0] == sol[-1]:
                continue
            elif (m == -1 or C[j][1] > C[m][1]) and C[j][1] > 0:
                m = j
        if m == -1: return "IMPOSSIBLE"
        sol.append(C[m][0])
        C[m][1]-=1

    for i in range(len(sol)):
        if sol[i] == sol[i-1]: return "IMPOSSIBLE"

    return ''.join(sol)

T = input()

for t in range(1,T+1):
    print("Case #%d: %s" % (t,solve()))
