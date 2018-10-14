import sys

T=int(sys.stdin.readline())
for t in range(1, T+1):
    line=sys.stdin.readline()
    
    line=line.split(" ")
    sh=[int(x) for x in line[1].strip()]
    #print sh
    
    leftsum=0
    added=0
    for ind, val in enumerate(sh):
        if ind>leftsum:
            added+=(ind-leftsum)
            leftsum+=(ind-leftsum)
        leftsum+=val
    
    print "Case #"+str(t)+": "+str(added)
