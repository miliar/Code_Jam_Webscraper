import scipy

def gcd(vecty):
    vectyold=0
    while not(all(vecty==vectyold)):
        vecty.sort()
        vectyold=vecty
        vecty=vecty-scipy.append(0,vecty)[:-1]
    return max(vecty)

f=open('B-small-attempt2.in')
#f=open('B-bignums.in')
g=open('B-small-attempt2.out','w')
C=int(f.readline())

for c in range(1,C+1):
    gelist=[int(value) for value in f.readline().split()]
    N=gelist.pop(0)
    gelist.sort()
    ge=scipy.array(gelist)
    intervals=ge[1:]-ge[:-1]
    T = gcd(intervals)
    #print c,T
    
    apocalypse=-min(gelist)
    while apocalypse<0:
        apocalypse=apocalypse+T

##    apocalypse1=-gelist[0]
##    while apocalypse1<0:
##        apocalypse1=apocalypse1+T
##    apocalypse2=-gelist[1]
##    while apocalypse2<0:
##        apocalypse2=apocalypse2+T
##    apocalypse3=-gelist[-1]
##    while apocalypse3<0:
##        apocalypse3=apocalypse3+T
##    print apocalypse1-apocalypse2,apocalypse2-apocalypse3
    
    print >>g, "Case #"+str(c)+": "+str(apocalypse)

f.close()
g.close()

print "done!"
