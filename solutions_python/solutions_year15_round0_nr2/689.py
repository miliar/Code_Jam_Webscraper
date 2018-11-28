#!/usr/bin/python

infile = "B-small-attempt2.in"
#infile = "b-ex.in"

f    = open( infile )
fout = open( infile.replace("in","out") , "w" )

from math import *

T = int ( f.readline() )
verb = False

keep_eating = set()
skeep_eating = set()

def ssolve( diners, t = 0 ):

    m = max(diners) 
    n = diners.count(m)
     
    global best
    if False :
        print "SS", diners , t, "+", m , " =", t + m
        
    if (m,n) in skeep_eating : 
        print skeep_eating
        return t+m

    if m <= 3 : return t+m
    
    # either keep eating from now on
    
    a = [ t+m ]

    # or split the largest pile

    r =  int(sqrt(m))+1

    x1 = max( 2, m/2-r )
    
    for i in range( x1 , m/2 + 1) :# e.g. for 9 : go upto 4
        #print "m = ", m, i
        h1 = i
        h2 = m-i
        diners_ = diners[:]
        iii = diners_.index( m ) 
        diners_[iii] -= h2
        diners_.append( h2 )
        
        a.append( ssolve ( diners_ , t+1 ) )

    ma = min(a)    
    #if ma == a[0] and a.count(ma) == 1:
        #print "S add", diners, a, "     ",m,n
        #skeep_eating.add( (m,n) )

    #print a
    return ma


def solve( diners, t = 0 ):

    m = max(diners) 
    n = diners.count(m)

    if verb: print "xx", diners , t, "+", m , " =", t + m

    if (m,n) in keep_eating : 
        #print m,n , " ----> keep eating "
        
        #print keep_eating
        return t+m

    
    if m <= 3 : return t+m
    #f m == 4 and n > 1 : return t+m # two fours : keep eating
     

    # either keep eating from now on
    
    a1 = t + m

    # or split the largest pile

    h1 = m/2
    h2 = m-h1
    diners_ = diners[:]
    iii = diners_.index( m ) 
    diners_[iii] -= h2
    diners_.append( h2 )
    a2 = solve ( diners_ , t+1 )

    if a1 < a2 : # remember that the solution is to keep eating
        #print "add", m,n
        keep_eating.add( (m,n) )

    return min( a1, a2 )
 
if False :   
    import sys
    for i in range(1,1000):
        print i
        best = solve([i])
        print best
        best2 =  ssolve([i])

        if best  != best2 : 
            print "differnce for" , i , best, best2

    sys.exit()


for i in range( 1, T+1 ):
    
    D  = int(f.readline()) 
    diners = [ int(x) for x in f.readline().split() ]

    #print 
    #print diners

    #ans = solve(diners)
    ans2 = ssolve(diners)
    #print "ppp", diners , " --> ", ans, ans2

    print "Case #%d: %s" % (i, ans2)
    fout.write( "Case #%d: %s\n" % (i, ans2))

fout.close()
