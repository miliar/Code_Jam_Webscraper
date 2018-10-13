def solve(R, C, M):
    A = set(c for r in M for c in r if c != '?')
    D = {t: [min(c for r in range(R) for c in range(C) if M[r][c] == t),
             min(r for r in range(R) for c in range(C) if M[r][c] == t),
             max(c for r in range(R) for c in range(C) if M[r][c] == t),
             max(r for r in range(R) for c in range(C) if M[r][c] == t)] for t in A}
    for t in A:
        for c in range(D[t][0], D[t][2]+1):
            for r in range(D[t][1], D[t][3]+1):
                M[r][c]=t
    try:
        e1 = min(r for r in range(R) for c in range(C) if M[r][c] == '?')
        e2 = min(c for c in range(C) if M[e1][c] == '?')
        E=[e2, e1]
    except:
        return '\n'+'\n'.join(''.join(r) for r in M)
    for t in A: 
        ND = [min(D[t][0],E[0]),min(D[t][1],E[1]),max(D[t][2],E[0]),max(D[t][3],E[1])]
        VIOLATE=False
        for t2 in A:
            if t2==t:
                continue
            AD = D[t2]
            if ND[0]<=AD[2] and ND[2]>=AD[0] and ND[1]<=AD[3] and ND[3]>=AD[1]:
                VIOLATE=True
                break
        if VIOLATE:
            continue
        AM = [[c for c in r] for r in M]
        AM[E[1]][E[0]]=t
        try:
            return solve(R, C, AM)
        except:
            pass
    raise BaseException()

cnt = int(input())
for i in range(cnt):
    R, C = input().split(' ')
    M=[input() for j in range(int(R))]
    print('Case #' + str(i+1) +': '+solve(int(R), int(C), [[c for c in r] for r in M]))