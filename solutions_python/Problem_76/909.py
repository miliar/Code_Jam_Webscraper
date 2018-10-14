import itertools
def findsubsets(t):
    S = set(range(0,t))
    res = set()
    for i in range(0,len(S)):
        res = res.union(set(itertools.combinations(S, i)))
    res.remove(())
    res = map(lambda x: (x, S.difference(x)), res)
    return res

def addGood(L1, L2):
    res = 0
    for i in L1:
        res = res + L2[i]
    return res

def addBad(L1, L2):
    res = 0
    for i in L1:
        res = res ^ L2[i]
    return res

def solver(S):
    L = map(int, S.split())
    max = 0
    subs = findsubsets(len(L))
    for sub in subs:
        if (addBad(sub[0], L) == addBad(sub[1], L)) and addGood(sub[0], L) > max :
            max = addGood(sub[0], L) 
        if (addBad(sub[1], L) == addBad(sub[0], L)) and addGood(sub[1], L) > max :
            max = addGood(sub[1], L)
    if max: return str(max)
    return 'NO'

results = map(solver, open("test.in", 'r').readlines()[1:][1::2])
for i in range(0, len(results)):
    print "Case #" + str(i+1) + ": " + results[i]

