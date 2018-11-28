T = int(raw_input())
for t in xrange(T):
    tokens = raw_input().split(' ')
    nonbases = []
    for i in xrange(int(tokens.pop(0))):
        nonbases.append(tokens.pop(0))
    opposites = []
    for i in xrange(int(tokens.pop(0))):
        opposites.append(tokens.pop(0))
    toinvoke = tokens[1]
    #print nonbases
    #print opposites
    #print toinvoke
    elist = []
    for e in toinvoke:
        elist.append(e)
        if len(elist) < 2:
            continue
        # combine
        while True:
            to_break = True
            for nb in nonbases:
                if (elist[-1] == nb[0] and elist[-2] == nb[1] or
                    elist[-1] == nb[1] and elist[-2] == nb[0]):
                    elist.pop()
                    elist[-1] = nb[2]
                    to_break = False
            if to_break:
                break
        # clear
        for o in opposites:
            if o[0] in elist and o[1] in elist:
                elist = []
                break
    print "Case #%d: %s" % (t + 1, str(elist).replace("'", ""))

