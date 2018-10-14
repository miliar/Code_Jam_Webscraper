import sys
from collections import defaultdict

def reduceList(combine, delete, s):
    l = []
    for c in s:
        l.append(c)
        if len(l) > 1:
            if (l[-1], l[-2]) in combine.keys():
                c = combine[(l[-1], l[-2])]
                l.pop()
                l.pop()                
                l.append(c)
            elif c in delete:
                if not delete[c].isdisjoint(set(l[:-1])):
                    l = []
    return '['+', '.join(l)+']'


def process(l):
    C = int(l[0])
    combine = {}
    for c in l[1:C+1]:
        combine[(c[0], c[1])] = c[2]
        combine[(c[1], c[0])] = c[2]
    D = int(l[1+C])
    delete = defaultdict(set)
    for d in l[2+C:2+C+D]:
        delete[d[0]].add(d[1])
        delete[d[1]].add(d[0])
    s = l[3+C+D]
    return reduceList(combine, delete, s)


T = int(sys.stdin.readline().strip())
for i in xrange(T):
    print "Case #%d:"%(i+1), process(sys.stdin.readline().strip().split(" "))
