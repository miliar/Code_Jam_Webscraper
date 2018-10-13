f = open("B-large.in")
fout = open("B.out", "w")

T = int(f.readline())
for t in xrange(T):
    v = f.readline().strip().split()
    
    combine = dict([(c, {}) for c in "QWERASDF"])
    oppose = dict([(c, set()) for c in "QWERASDF"])
    
    C = int(v[0])
    for c in v[1:C+1]:
        combine[c[0]][c[1]] = c[2]
        combine[c[1]][c[0]] = c[2]

    D = int(v[C+1])
    for d in v[C+2:C+D+2]:
        oppose[d[0]].add(d[1])
        oppose[d[1]].add(d[0])

    spell = v[C+D+3]
    
    line = []
    for c in spell:
        if line:
            last = line[-1]
            if last in combine and c in combine[last]:
                line[-1] = combine[last][c]
                continue
        
        line.append(c)

        if any([e in oppose[c] for e in line]):
            line = []
    
    print >>fout, "Case #%d: [%s]" % (t+1, ", ".join(line))
    