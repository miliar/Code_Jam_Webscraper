from bisect import*

FILE = "P1_small"
try:
    inFile = open(FILE+".txt")
except:
    pass

def read():
    try:
        return inFile.readline().strip()
    except:
        return raw_input().strip()


out = open("P1.out","w")
cases = int(read())
for case in xrange(cases):
    n,m = map(int,read().split())
    
    normal = 0
    left = []
    right = []
    for _ in xrange(m):
        l,r,x = map(int,read().split())
        left.extend([l]*x)
        right.extend([r]*x)
        d = r-l
        normal += d*(d-1)/2*x
        
    left.sort()
    right.sort()
    #print left
    #print right
    best = 0
    for l in reversed(left):
        i = bisect_left(right,l)
        r = right[i]
        d = r-l
        #print l,r
        best += d*(d-1)/2
        del right[i]
        
    print best-normal
    #print "\n"
    out.write("Case #%i: %i\n" %(case+1,best-normal))