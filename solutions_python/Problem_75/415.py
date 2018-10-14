from sys import stdin

for case in range(1, int(stdin.readline()) + 1):
    inp = stdin.readline().split()
    comb = {}
    c = int(inp[0])
    for i in range(1, c+1):
        comb[inp[i][:2]] = inp[i][2]
        comb[inp[i][1::-1]] = inp[i][2]
    inp = inp[c+1:]
    oppos = {'Q': set(),'W': set(),'E': set(),'R': set(),
             'A': set(),'S': set(),'D': set(),'F': set()}
    d = int(inp[0])
    for i in range(1, d+1):
        oppos[inp[i][0]].add(inp[i][1])
        oppos[inp[i][1]].add(inp[i][0])

    seq = inp[d+2]
    l = []
    for e in seq:
        if l != []:
            comb_key = ''.join([l[-1], e])
            if comb_key in comb:
                l[-1] = comb[comb_key]
                continue
            elif len(oppos[e].intersection(l)) > 0:
                l = []
                continue
        l.append(e)

    print "Case #%d: [%s]" % (case, ", ".join(l))
