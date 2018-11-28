import sys


M = [
    [ 0, 1, 2, 3 ],
    [ 1, 0, 3, 2 ],
    [ 2, 3, 0, 1 ],
    [ 3, 2, 1, 0 ]
]
Z = [
    [ 1, 1, 1, 1 ],
    [ 1, -1, 1, -1 ], 
    [ 1, -1, -1, 1 ],
    [ 1, 1, -1, -1 ]
]

def mul( x, y ):
    sign, x = x
    return sign*Z[x][y], M[x][y]


def solve( L, X, S ):
    S = [ ord(i)-104 for i in S.strip() ] * X
    #print S
    x = (1, 0)
    target = [ (1, 3), (1,2), (1,1) ]
    r = (1, 0)
    for y in S:
        if len(target)>0:
            #print x, y, mul( x, y )
            x = mul( x, y )
            if x == target[-1]:
                x = r
                target.pop()
        else:
            r = mul( r, y )
    if len(target)==0 and r==(1,0):
        return "YES"
    else:
        return "NO"

def main():
    f = open(sys.argv[1])
    T = int( f.next() )
    for i in range(T):
        L, X = map( int, f.next().split() )
        print "Case #{0}: {1}".format( i+1, solve( L, X, f.next() ) )

main()


