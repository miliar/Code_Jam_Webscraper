from math import log2

def solve():
    n,k= [int(e) for e in input().split()]
    m = int(log2(k))
    d = 2**m - 1
    s = int( (n-d)/ (d+1) )
    r = (n-d) % (d+1)

    if r > k - d - 1:
        maxd = int( (s+1)/2)
        mind = int( s/2 )
    
    else:
        maxd = int(s/2)
        mind = int((s-1)/2)
        
    return str(maxd) + " " + str(mind)

T=int(input());
 
for t in range(1,T+1):
    print ("Case #" + str(t) + ": " + solve())
