import sys
import copy

def war(naomi, ken):
    naomi = set(naomi)
    ken = set(ken)
    score_n = 0
    while naomi:
        n = naomi.pop()
        if n > max(ken):
            k = min(ken)
            ken.remove(min(ken))
            score_n += 1
        else:
            k = min(k for k in ken if k > n)
            ken.remove(k)
    return score_n

def deceitful_war(naomi, ken):
    naomi = set(naomi)
    ken = set(ken)
    score_n = 0
    while naomi:
        k = min(ken)
        if max(naomi) > k:
            naomi.remove(min(n for n in naomi if n > k))
            ken.remove(k)
            score_n += 1
        else:
            naomi.remove(min(naomi))
            ken.remove(max(ken))
    return score_n
    

with open(sys.argv[1]) as f:
    T = int(f.readline())

    for case in xrange(T):
        N = int(f.readline().strip())
        naomi = [ float(field) for field in f.readline().strip().split() ]
        ken = [ float(field) for field in f.readline().strip().split() ]
        naomi.sort()
        ken.sort()
            
        print "Case #%d:" % (case + 1),
        print deceitful_war(naomi, ken),
        print war(naomi, ken)

        
