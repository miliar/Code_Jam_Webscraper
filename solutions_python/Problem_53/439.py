#import sys
#g=sys.stdout
g=open('A-large.out','w')
f=open('A-large.in')
T=int(f.readline())
for t in range(1,T+1):
    print >>g, "Case #"+str(t)+":",
    N,K=[int(value) for value in f.readline().split()]
    if (not (K+1) % (2**N)):
        print >>g, "ON"
    else:
        print >>g, "OFF"
    
f.close()
g.close()

print "done!"
