for t in range(int(raw_input())):
    
    r, k, n = [int(i) for i in raw_input().split()]
    g = [int(i) for i in raw_input().split()]

    sol, fsol = 0, 0
    if sum(g) <= k:
        fsol = sum(g)*r
    else:
        for i in range(r):
            while sol <= k:
                tmp = g.pop(0)
                g.append(tmp)
                sol += tmp
            if sol <= k:
                fsol += sol
                sol = 0
            else:
                fsol += sol - tmp
                sol = tmp

    print "Case #" + str(t+1) + ": " + str(fsol)


