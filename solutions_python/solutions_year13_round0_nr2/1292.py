for T in range(int(raw_input())):
    H,W = map(int,raw_input().strip().split())
    m = [[int(x) for x in raw_input().split()] for y in range(H)]
    minv = [[m[y][x] for y in range(H)] for x in range(W)]
    imposs = False
    for y in range(H):
        for x in range(W):
            if min(max(m[y]), max(minv[x])) > m[y][x]:
                imposs = True
                break
        if imposs: break
    print("Case #%d: %s" % (T+1, ("NO" if imposs else "YES")))
