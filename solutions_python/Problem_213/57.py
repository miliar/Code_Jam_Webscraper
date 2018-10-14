def Solve(N, p1, p2):
    p1.sort();
    p2.sort();
    
    pos1s = 0;
    for pos in p1 + p2:
        if pos == 1:
            pos1s += 1;

    if pos1s >= max(len(p1), len(p2)):
        print pos1s, 0
        return;
    
    TotalRides = max(pos1s, len(p1), len(p2));
    Promotions = 0;
    
    while min(len(p1), len(p2)) != 0:
        min1 = min(p1);
        e2 = -1;

        for e in p2:
            if (e2 == -1) and (e != min1) and (e in p1):    # remove a future problem
                e2 = e;

        if (e2 == -1):
            for e in p2:
                if (e2 == -1) and (e != min1):    # remove a future problem
                    e2 = e;

        if (e2 != -1):
            p1.remove(min1);
            p2.remove(e2);

        else:   # Can remove nothing from P2
            if len(p1) > len(p2):
                p1.remove(min1);
            else:
                p1.remove(min1);
                p2.remove(p2[0]);
                Promotions += 1;

    print TotalRides, Promotions


T = int(raw_input());
for q in range(T):
    [N, C, M] = map(int, raw_input().split());

    P1 = [];
    P2 = [];
    for i in range(M):
        [pi, bi] = map(int, raw_input().split());
        
        if (bi == 1):
            P1.append(pi);
        else:
            P2.append(pi);

    print "Case #%d:" % (q+1),

    if len(P1) < len(P2):
        Solve(N, P2, P1);
    else:
        Solve(N, P1, P2);

