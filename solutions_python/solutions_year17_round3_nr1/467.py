T = int(input())
for t in range(T):
    n, k = input().split()
    n, k = [int(n), int(k)]
    S = []
    Sr = []
    for ni in range(n):
        r, h = input().split()
        r, h = [int(r), int(h)]
        S.append((r, h, ni))
        Sr.append((r, ni))
    S2 = sorted(S, key = lambda v: -v[0] * v[1])
    Sr.sort(key = lambda v: -v[0])
    res = 0
    #print(S)
    #print(S2)
    #print(Sr)
    for i in range(n - k + 1):
        c = 0
        j = 0
        s = Sr[i][0]**2 + 2 * S[Sr[i][1]][0] * S[Sr[i][1]][1]
        while c < k - 1:
            if S2[j][0] <= Sr[i][0] and S2[j][2] != Sr[i][1]:
                s += 2 * S2[j][0] * S2[j][1]
                c += 1
            j += 1
        res = max(res, s)
    print("Case #" + str(t + 1) + ": " + str(3.14159265358 * res))
            
