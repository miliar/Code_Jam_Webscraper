cases = raw_input()
for case in xrange(int(cases)):
    l = raw_input().strip().split()
    
    comb = {}
    opp = []
    for i in xrange(int(l.pop(0))):
        comb[l[0][:2]] = l[0][-1]
        comb[l[0][1]+l[0][0]] = l[0][-1]
        l.pop(0)
    for i in xrange(int(l.pop(0))):
        opp.append(l[0])
        opp.append(l[0][::-1])
        l.pop(0)
        
    n = l.pop(0)
    call = l.pop(0)
    out = []
    for i in call:
        if len(out) == 0:
            out.append(i)
        elif out[-1]+i in comb:
            out[-1] = comb[out[-1]+i]
        else:
            for j in xrange(len(out)):
                if out[j]+i in opp:
                    out = []
                    i = None
                    break
            if i != None:
                out.append(i)

    output = '[]'
    for i in out:
        output = '[%s]' % ', '.join(out)
        
    print 'Case #%d: %s' % (case + 1, output)
