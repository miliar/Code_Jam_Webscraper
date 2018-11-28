import sys

it = (e.strip() for e in  sys.stdin)

for i in range(int(it.next())):
    vSize = int(it.next())
    vect1 = sorted([int(e) for e in it.next().split(" ")])
    vect2 = sorted([int(e) for e in it.next().split(" ")], lambda a, b: cmp(b,a))
    print "Case #%i: %i" % (i+1, sum(a*b for a, b in zip(vect1, vect2)))
            
    
    
    