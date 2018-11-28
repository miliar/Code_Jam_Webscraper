import sys
from bisect import bisect

T = int(sys.stdin.readline())
for case in xrange(T):
    R, k, N = [int(x) for x in sys.stdin.readline().split(' ')]
    g = [int(x) for x in sys.stdin.readline().split(' ')]
   
    if( sum(g) <= k ): 
        ret = sum(g)*R
    else:
        s = [ 0 ]
        for i in xrange(0, N): s.append(s[-1] + g[i])
        for i in xrange(0, N): s.append(s[-1] + g[i])

        seen = {}

        ret = 0
        a = 0
        
        while R > 0:
            b = bisect(s, s[a] + k)-1
            ret += s[b] - s[a]
            a = b % N
            R -= 1            
                        
            if(seen.has_key(a)):
                cyclelen, add = seen[a][0] - R, ret - seen[a][1]
                cycles = R / cyclelen
                
                R -= cycles * cyclelen
                ret += cycles * add
            else:
                seen[a] = (R, ret)
    
    print "Case #{0}: {1}".format(case+1, ret)