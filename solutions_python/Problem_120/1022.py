test = open("C:/Users/Laszlo/Documents/Program/Python/CodeJam/2013/Round1A/A-small-attempt1.in")
out = open("C:/Users/Laszlo/Documents/Program/Python/CodeJam/2013/Round1A/out.out ", "w+")
from math import sqrt, floor

T = int(test.readline())

for i in xrange(T):
    r, t = tuple([int(x) for x in test.readline().split()])
    n=0
    while True:
        pai = 2*n**2 + (2*r-1)*n
        if pai>t:
            break
        n+=1
    n-=1
    out.write("Case #%d: %d\n"%(i+1,n))

test.close()
out.close()
