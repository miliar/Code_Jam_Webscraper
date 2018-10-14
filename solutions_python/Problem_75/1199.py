for case in xrange(input()):
    l = raw_input().split()
    c = int(l[0])
    d = int(l[c+1])
    n = int(l[c+d+2])
    combs = {b:{} for b in ['Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F']}
    for s in l[1:c+1]:
        combs[s[0]][s[1]] = s[2]
        combs[s[1]][s[0]] = s[2]
    opps = {b:set() for b in ['Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F']}
    for s in l[c+2:c+d+2]:
        opps[s[0]].add((s[1]))
        opps[s[1]].add((s[0]))
    o = []
    for s in list(l[-1]):
        if not o:
            o.append(s)
        elif o[-1] in combs[s]:
            o[-1] = combs[s][o[-1]]
        elif opps[s] & set(o):
            o = []
        else:
            o.append(s)
    print "Case #%d:" % (case+1), str(o).replace("'","")
