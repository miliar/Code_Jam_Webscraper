from numpy import *

file = open("A-large.in")
n = int(file.readline())
#print n
out = open("1.out","wt")
import re
for x in range(0,n):
    s = int(file.readline())
    print s
    engines = []
    for y in range(0,s):
        engines.append(re.sub("\n|\r","",file.readline()))
    print engines
    q = int(file.readline())
    print q
    queries = []
    if q == 0:
        print "Case #%d: %d\n"% (x+1,0)
        out.write("Case #%d: %d\n"% (x+1,0))
    else:
        for y in range(0,q):        
            queries.append(re.sub("\n|\r","",file.readline()))
        print queries
        dp = zeros( (q+1,s), dtype=int )
        for q in range(1,len(queries)):
            for e in range(0,len(engines)):
                dp[q][e] = 10000;
    
        for e in range(0,len(engines)):
            if queries[0] == engines[e]:
                dp[0][e]=10000
    
        for q in range(1,len(queries)):
            for e in range(0,len(engines)):
                if queries[q] != engines[e]:
                    dp[q][e] = dp[q-1][e]
                    for z in range(0,len(engines)):
                            dp[q][e] = min(dp[q][e],dp[q-1][z] + 1)
                            
                elif queries[q] == engines[e]:
                    dp[q][e] = 10000;
                    #for z in range(0,len(engines)):
                    #    if z!= e:
                    #        dp[q][e] = min(dp[q][e],dp[q-1][z] + 1)
        print dp
        ans = 10000
        for z in range(0,len(engines)):
            ans = min(ans,dp[q][z])
        print "Case #%d: %d"% (x+1,ans)
        out.write("Case #%d: %d\n"% (x+1,ans))

