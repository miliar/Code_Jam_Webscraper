# -*- coding: utf-8 -*-
# Uses https://github.com/rkistner/contest-algorithms


def mycmp(a, b):
    #v1 = a.l*a.p + b.l*(1 - (1-a.p)*(1-b.p))
    #v2 = b.l*b.p + a.l*(1 - (1-a.p)*(1-b.p))
    v1 = a.l + a.p * (a.l + b.l)
    v2 = b.l + b.p * (a.l + b.l)
#    if v1 == v2:
#        return a.i - b.i
#    else:
#        return v1-v2
    return v1-v2

class K(object):
    def __init__(self, l, p, i):
        self.l = l
        self.p = p
        self.i = i

    def __lt__(self, other):
        return mycmp(self, other) < 0
    def __gt__(self, other):
        return mycmp(self, other) > 0
    def __eq__(self, other):
        return mycmp(self, other) == 0
    def __le__(self, other):
        return mycmp(self, other) <= 0
    def __ge__(self, other):
        return mycmp(self, other) >= 0
    def __ne__(self, other):
        return mycmp(self, other) != 0




import sys
fin = sys.stdin
T = int(fin.readline())
for case in range(1,T+1):
    N = int(fin.readline())
    L = list(map(int, fin.readline().split()))
    P = list(map(int, fin.readline().split()))
    #print(L, file=sys.stderr)
#    k = []
#    for i, l_p in enumerate(zip(L, P)):
#        k.append(K(l_p[0], 1- l_p[1]/100, i))
#    k.sort()
    q = [(100-p, i) for i, p in enumerate(P)]
    q.sort()
    #combined = list(enumerate(zip(L, P)))
    #combined.sort(key=cmp_to_key(cmp))
    #q = [(-l_p[0]*(l_p[1]), i) for i, l_p in enumerate(zip(L, P))]
    #q.sort()
    result = [str(i) for v, i in q]

    print(q, file=sys.stderr)
    print("Case #%d: %s" % (case, " ".join(result)))

