import sys
import psyco
psyco.full()

pattern="welcome to code jam"

N=int(sys.stdin.readline())
for i in range(N):
    code=[0]*(len(pattern)+1)
    code[0]=1
    
    S=sys.stdin.readline()
    for char in S:
        for j in range(len(pattern),0,-1):
            if pattern[j-1]==char:
                code[j]+=code[j-1]
                code[j]%=10000
    
    print "Case #%d: %04d"%(i+1,code[len(pattern)])