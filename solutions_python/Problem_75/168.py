T = input()
for t in range(T):
    combs = {}
    opps = {}
    pres = {}

    toks = raw_input().split()
    C = int(toks[0])
    for i in range(1, C+1):
        combs[toks[i][:2]] = combs[toks[i][-2::-1]] = toks[i][2]

    D = int(toks[C+1])
    for i in range(C+2, D+C+2):
        c1, c2 = toks[i]
        if not c1 in opps:
            opps[c1] = ''
        if not c2 in opps:
            opps[c2] = ''

        opps[c1] += c2
        opps[c2] += c1

    seq = toks[-1]
    res = []
    for c in seq:
        cb = res[-1] + c if res else '#'
        if cb in combs:
            pres[res[-1]] -= 1
            res.pop()
            res.append(combs[cb])
        elif [x for x in opps if x in pres and pres[x] > 0 and c in opps[x]]:
            res = []
            pres = {}
        else:
            res.append(c)
            if not c in pres:
                pres[c] = 0
            pres[c] += 1

    print 'Case #%d: [%s]' % (t+1, ', '.join(res))

