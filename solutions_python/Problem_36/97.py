import sys,re
import string
f=open( sys.argv[1])
N=int(f.readline().strip())
for n in xrange(N):
    X=f.readline().strip()
    Y="welcome to code jam"
    dp=[]
    dp.append([1]*(len(X)+1))
    for y in range(1,len(Y)+1):
        dp.append([0]*(len(X)+1))
        for x in range(1,len(X)+1):
            if X[x-1]==Y[y-1]:
                dp[y][x]=(dp[y-1][x]+dp[y][x-1] )% 10000
            else:
                #print y,x
                dp[y][x]=dp[y][x-1] % 10000 


    print "Case #%d: %04d" % (n+1 , dp[len(Y)][len(X)])

