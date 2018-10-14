import math
from sys import stdin as fp

def solve(L):
    uniqs = []
    for i, s in enumerate(L):
        c = None
        num = 0
        uniq = []
        j = 0
        while j < len(s):
            k = j
            while k < len(s) and s[k] == s[j]:
                k+=1
            uniq.append((s[j], k-j))
            c = s[j]
            j = k
        uniqs.append(uniq)
        if len(uniqs) > 1 and not first_el_comp(uniqs[-1], uniqs[-2]):        
            return None
    actions = []
    for i in xrange(len(uniqs[0])):
        lens = [uniq[i][1] for uniq in uniqs]
        ideal = int(math.ceil(sum(lens)/len(L)*1.0))
        
        actions.append(min(actions_for_char(lens, ideal), actions_for_char(lens, ideal)))
    
    return sum(actions)
    
def actions_for_char(L, x):
    return sum(abs(i - x) for i in L)

    
def first_el_comp(l1,l2):
    if len(l1 )!= len(l2): return False
    for t1, t2 in zip(l1,l2):
        el1, _ = t1
        el2, _ = t2
        if el1 != el2:
            return False
    return True
    
T = int(fp.readline())
for i in xrange(T):
    N = int(fp.readline())
    L = []
    for j in xrange(N):
        L.append(fp.readline().strip())
    solution = solve(L)
    print "Case #%s: %s" % (i +1, "Fegla Won" if solution is None else solution)
