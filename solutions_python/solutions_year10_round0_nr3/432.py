from math import *

    ##g=[1,4,2,1]
    ##R=4
    ##k=6
    ##N=4

##    g=[2,4,2,3,4,2,1,2,1,3]
##    R=5
##    k=5
##    N=10

    ##g=[1]
    ##R=100
    ##k=10
    ##N=1

f=open('C-small-attempt0.in')
h=open('C-small-attempt0.out','w')
T=int(f.readline())

for t in range(1,T+1):

    R,k,N=[int(value) for value in f.readline().split()]
    g=[int(value) for value in f.readline().split()]
    
    # find a cycle
    rides=0
    E=0
    i=0
    while rides<R:
        j=0
        # fill up one ride:
        e=0
        next_group=0
        while j<N:
            next_group=g[i]
            e=e+next_group
            if e>k:
                e=e-next_group
                break
            #print i,e,j
            i=i+1
            if i==N:
                i=0 # wrap round
            j=j+1
        E=E+e
        rides=rides+1
        #print i
        if i==0: # i.e. first group on next ride will be g[0]
            break

    cycles = int(floor(R/rides))
    rides_left = R - cycles*rides

    # do last little bit
    i=0
    E_left=0
    e=0
    for r in range(0,rides_left):
        j=0
        e=0
        next_group=0
        while j<N:
            next_group=g[i]
            e=e+next_group
            if e>k:
                e=e-next_group
                break
            i=i+1
            if i==N:
                i=0 # wrap round
            j=j+1
        E_left=E_left+e

    E_total = cycles*E + E_left

    print >>h, "Case #"+str(t)+": "+str(E_total)

f.close()
h.close()

print "done!"
