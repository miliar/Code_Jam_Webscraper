import sys

def game(x,r,c):
    if x == 1:
        return 1
    if x == 2:
        if min(r,c)==1 and max(r,c)==2:
            return 1
    if x == 4:
        if (min(r,c)==2 and max(r,c)==4):
            return 0
    if (r*c) <= x or (r*c)%x != 0:
        return 0
    return 1
        

for cases in xrange(int(sys.stdin.readline())):
    x,r,c = map(int,sys.stdin.readline().split())
    if game(x,r,c) == 1:
        ans = "GABRIEL"
    else:
        ans = "RICHARD"
    print "Case #%d: %s"%(cases+1,ans)
