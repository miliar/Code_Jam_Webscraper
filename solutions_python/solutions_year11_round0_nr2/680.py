import sys, re

base = set(['Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'])

def solve(line, casenum):
    res = []
    combs = {}
    opps = {}   
    for e in base:
        combs[e] = {}
        opps[e] = set([])
    null, comb, opp, elem = map(lambda s: s.strip(), re.split(r'\d+', line))
    if comb:
        for c in comb.split(' '):
            e1, e2, r = list(c)
            combs[e1][e2] = r
            combs[e2][e1] = r
    if opp:
        for o in opp.split(' '):
            e1, e2 = list(o)
            opps[e1].add(e2)
            opps[e2].add(e1)
    for e in elem:
        if not res:
            res.append(e)
            continue
        if combs[e].has_key(res[-1]):
            res[-1] = combs[e][res[-1]]
            continue
        if any(map(lambda r: r in opps[e], res)):
            res = []
            continue
        res.append(e)
    print "Case #%d: [%s]" % (casenum + 1, ', '.join(res))

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        lines = f.readlines()
        lines = lines[1:]
        for i in xrange(len(lines)):
            solve(lines[i], i)
