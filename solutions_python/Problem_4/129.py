import sys
T=int(sys.stdin.readline().rstrip())
for i in range(T):
    n=int(sys.stdin.readline().rstrip())
    v1=map(int,sys.stdin.readline().split())
    v2=map(int,sys.stdin.readline().split())
    v1.sort()
    v2.sort()
    v2.reverse()
    #print n
    #print v1
    #print v2
    assert len(v1)==n and len(v2)==n
    print "Case #%d: %d"%(i+1,sum(map(lambda x,y:x*y,v1,v2)))