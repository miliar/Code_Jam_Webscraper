from copy import deepcopy
casenum = 1

def doit(case):
    origcase = deepcopy(case)
    global casenum
    case = case.split(' ')[::-1]
    C = int(case.pop())
    combos = {}
    for i in range(C):
        combo = case.pop()
        combos[''.join(sorted(combo[:2]))] = combo[2]

    D = int(case.pop())
    opps = []
    for i in range(D):
        opps.append(''.join(sorted(case.pop())))

    N = case.pop()
    seq = case.pop()
        
    #print '(', origcase, ') :', C, combos, D, opps, N, seq

    res = []
    for c in seq:
        res.append(c)

        if len(res) >= 2:
            key = ''.join(sorted(res[-2:]))
            if key in combos:
                new = combos[key]
                res.pop()
                res.pop()
                res.append(new)

        if len(res) >= 2:
            for r in res[:-1]:
                if ''.join(sorted([r,res[-1]])) in opps:
                    res = []
                    break

    print 'Case #%d: [%s]' % (casenum, ', '.join(res))
    casenum += 1
            

raw = [x.strip() for x in open('B-large.in').readlines()]
ZZZ = int(raw[0])
data = raw[1:]
for case in range(ZZZ):
    doit(data[case])
