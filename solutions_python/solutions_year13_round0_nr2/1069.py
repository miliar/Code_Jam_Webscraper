T = input()
for i in range(T):
    N, M = [int(x) for x in raw_input().split()]
    grass =[[int(x) for x in raw_input().split()] for j in range(N)]
    yes = True
    for j in range(N):
        for k in range(M):
            ok = True
            for l in range(N):
                if grass[j][k] < grass[l][k]:
                    ok = False
                    break
            if not ok:
                ok = True
                for l in range(M):
                    if grass[j][k] < grass[j][l]:
                        ok = False
                        break
            if not ok:
                yes = False
    if yes:
        print 'Case #'+str(i+1)+': YES'
    else:
        print 'Case #'+str(i+1)+': NO'
