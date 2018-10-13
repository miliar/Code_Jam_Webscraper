import math

def pd(l):
    a = 1
    for i in l:
        a *= i
    return a

for case in range(1, int(raw_input())+1):
    print "Case #%d: "%case, 
    n, k = map(int, raw_input().split())
    u = float(raw_input())
    p = map(float, raw_input().split())
    p.sort()
    pp = p[0]
    ans = pd(p)
    #print p
    for i, v in enumerate(p[1:]):
        #print u, pp
        if u >= (i+1)*(v-pp):
            u -= (i+1)*(v-pp)
            #print v, u
            pp = v
        else:
            ans = pd([pp+u/(i+1)]*(i+1)+p[i+1:])
            break
    else:
        v = 1
        i = len(p)
        ans = pd([pp+u/i]*i)



    print "%.9lf"%min(ans, 1)


        
