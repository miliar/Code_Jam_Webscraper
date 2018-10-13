for case in range(int(input())):
    n, k = map(int, input().split())

    l_s = [i for i in range(n)]
    r_s = [i for i in range(n-1, -1, -1)]
    
    available = set(range(n))
    for _ in range(k):
        maxx = max(min(l_s[s], r_s[s]) for s in available)
        cands = [s for s in available if min(l_s[s], r_s[s]) == maxx]

        if len(cands) >= 1:
            maxx = max(max(l_s[s], r_s[s]) for s in cands)
            cands = [s for s in cands if max(l_s[s], r_s[s]) == maxx]

        if len(cands) >= 1:
            cands = [cands[0]]

        s = cands[0]
        available.remove(s)

        i = s+1
        ct = 0
        while i < n and i in available:
            l_s[i] = ct
            ct += 1
            i += 1

        i = s-1
        ct = 0
        while i >= 0 and i in available:
            r_s[i] = ct
            ct += 1
            i -= 1


    print('Case #%d: %d %d' % (case+1, max(l_s[s], r_s[s]), min(l_s[s], r_s[s])))
