#! /usr/bin/python
# -*- coding:utf-8

import sys


def getd( center, v, t ):
    c1 = center[0] + v[0]*t
    c2 = center[1] + v[1]*t
    c3 = center[2] + v[2]*t
    return ( c1**2 + c2**2 + c3**2) ** 0.5


def geta( fs ):

    center = [0.,0.,0.]
    v = [0.,0.,0.]
    num = 1.0*len(fs);
    for f in fs:
        num += 1
        center[0] += f[0]
        center[1] += f[1]
        center[2] += f[2]
        v[0] += f[0+3]
        v[1] += f[1+3]
        v[2] += f[2+3]
    center[0] /= num
    center[1] /= num
    center[2] /= num
    v[0] /= num
    v[1] /= num
    v[2] /= num


    #vv = abs(v[0]**2 + v[1]**2 + v[2]**2)**(0.5)
    vv = abs( (v[1]*v[0])**2. + (v[1]*v[2])**2. + (v[0]*v[2])**2. )**(0.5)

    low = 0;
    high = 1000000000000000.
    for i in xrange(100000):
        m1 = (2*low+high)/3.
        m2 = (low+2*high)/3.
        d1 = getd(center, v, m1)
        d2 = getd(center, v, m2)
        if d1 > d2:
            low = m1
        else:
            high = m2

        if abs(low - high) <= 0.0000000001:
            break;        
        #print low, high
    #print low

    res = (d1+d2)

    #d = abs( v[2]*v[1]*center[0] + v[0]*v[2]*center[1] + v[0]*v[1]*center[2]   )/vv
    #d = abs( v[2]*v[1]*center[0] + v[0]*v[2]*center[1] + v[0]*v[1]*center[2]   )/vv
    
    return  res, (low+high)/2


def main( file ):
    f = open( file )
    T = int( f.readline().strip() )
    for t in range(T):
        N = int( f.readline().strip() )
        fs = [ map( int, f.readline().strip().split() ) for i in range( N ) ]
        print "Case #%d:" % (t + 1),
        print " %.8f %.8f" % geta( fs )
        #print "\n".join( [ " ".join( ans[y] ) for y in range(len(ans)) ] )
        
if __name__ == '__main__': main(sys.argv[1])

