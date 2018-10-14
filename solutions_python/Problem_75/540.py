T = input()
for i in xrange(T):
    line = raw_input().split()
    C = int(line.pop(0))
    combs = {}
    for c in xrange(C):
        comb = line.pop(0)
        combs[frozenset(comb[:2])] = comb[2]
    opps = {}
    D = int(line.pop(0))
    for d in xrange(D):
        opp = line.pop(0)
        opps[opp[0]] = opp[1]
        opps[opp[1]] = opp[0]
    N = int(line.pop(0))
    elems = line.pop(0)
    ans = []
    for e in elems:
        if len(ans) == 0:
            ans.append(e)
        elif frozenset(ans[-1] + e) in combs:
            c = combs.get(frozenset(ans[-1] + e))
            ans[-1] = c
        elif opps.get(e) in ans:
            ans = []
        else:
            ans.append(e)
    print "Case #%d: %s" % (i + 1, "[%s]" % ", ".join(ans))