#!/usr/bin/env python

def _combinators(_handle,items,n):
    if n==0:
        yield []
        return
    for i, item in enumerate(items):
        this_one = [item]
        for cc in _combinators(_handle,_handle(items,i),n-1):
            yield this_one + cc
            
def uniqueCombinations(items,n):
    def afterIthItem(items,i):
        return items[i+1:]
    return _combinators(afterIthItem,items,n)

def tri( X1,X2,X3 ):
    x1 = X1[0]
    x2 = X2[0]
    x3 = X3[0]
    y1 = X1[1]
    y2 = X2[1]
    y3 = X3[1]
    v1 = ( float(x1 + x2 + x3) / 3 , float(y1 + y2 + y3) / 3 )
    v2 = ( int ( (x1 + x2 + x3) / 3 ) , int ( float(y1 + y2 + y3) / 3 ) )
    return ( v1 == v2 )

def do_trial(f):
    line = [int(x) for x in f.readline().split()]
    n = line[0]
    A = line[1]
    B = line[2]
    C = line[3]
    D = line[4]
    X0= line[5]
    Y0= line[6]
    M = line[7]
    #print n,A,B,C,D,X0,Y0,M
    
    X = X0
    Y = Y0
    pointset = []
    pointset.append( ( X0 , Y0 ) )
    for i in range( 1 , n ):
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        pointset.append( ( X, Y ) )

    #print pointset

    count = 0
    for i in uniqueCombinations( pointset , 3 ):
        #print i,tri( i[0] , i[1] , i[2] )
        if tri( i[0] , i[1] , i[2] ) == True: count = count + 1
    return count        

#f = sys.stdin
f = open("A-small-attempt0.in")
T = int(f.readline())
for i in xrange(T):
    v = do_trial(f)
    print "Case #%d: %d" % (i+1,v)