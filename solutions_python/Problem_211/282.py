def small(n, k, u, lp_):
    lp = lp_[:]
    lp.sort()
    lp.append(1)
    i = 0
    mult = 1
    while u > 0 and i < n:
        d = lp[i+1]-lp[i]
        if d:
            if mult*d < u:
                #print "suf u", u, d, mult
                #print "before", lp
                u -= mult*d
                for j in range(i+1-mult,i+1):
                    lp[j] += d
                mult += 1
                #print "after", lp
            else:
                #print "insuf u", u, d, mult
                #print "before", lp
                for j in range(i+1-mult,i+1):
                    lp[j] += u/mult
                u = 0
                #print "after", lp
                break
        else:
            #print "mult", mult, mult+1
            mult += 1
        #print "next"
        i += 1
    return round(reduce(lambda x,y: x*y, lp), 6)

import sys
def read(conv = int):
    return map(conv, raw_input().strip().split())

for i in range(input()):
    N, K = read()
    U = input()
    lp = read(float)
    print "Case #{}: {}".format(i+1, small(N, K, U, lp))
    print >> sys.stderr, "Case #{}: {}".format(i+1, small(N, K, U, lp))
