import sys
from itertools import combinations_with_replacement

normopts = [x for x in list(combinations_with_replacement(range(11), 3)) if max(x) - min(x) <= 1]
wsupopts = [x for x in list(combinations_with_replacement(range(11), 3)) if max(x) - min(x) <= 2]

# builds map of sum -> best score
def buildmap(opts):
    map = {}
    for tup in opts:
        if sum(tup) not in map or map[sum(tup)] < max(tup):
            map[sum(tup)] = max(tup)

    return map

normmap = buildmap(normopts)
wsupmap = buildmap(wsupopts)


cases = int(sys.stdin.readline())

for i in range(1, cases + 1):
    caseinfo = [int(x) for x in sys.stdin.readline().split()]

    googlers = caseinfo[0]
    surprises = caseinfo[1]
    atleast = caseinfo[2]

    totals = caseinfo[3:]

    normal = [x for x in totals if normmap[x] >= atleast]
    wsurprise = [x for x in totals if wsupmap[x] >= atleast and normmap[x] < atleast]

    result = len(normal) + min(len(wsurprise), surprises)

    #print normal
    #print wsurprise

    print "Case #%d: %d" % (i, result)
