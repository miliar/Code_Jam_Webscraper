import sys

def solve( X, R, C ):
    if X == 1:
        return "GABRIEL"
    if X == 2:
        if (R&1)==0 or (C&1)==0:
            return "GABRIEL"
    if X == 3:
        if R==1 or C==1:
            return "RICHARD"
        if (R*C) % 3 != 0:
            return "RICHARD"
        return "GABRIEL"
    if X == 4:
        if (R*C) % 4 != 0:
            return "RICHARD"
        if R<=2 or C<=2:
            return "RICHARD"
        return "GABRIEL"
    return "RICHARD"

def main():
    f = open(sys.argv[1])
    T = int( f.next() )
    for i in range(T):
        X, R, C = map( int, f.next().split() )
        print "Case #{0}: {1}".format( i+1, solve( X, R, C ) )

main()


