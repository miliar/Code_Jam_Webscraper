#!/usr/bin/python

def main():
    with open("A-large.in") as f:
        T = int(f.readline().strip())

        for Tcur in range(1, T+1):
            args = [ list(f.readline().rstrip()) for i in range(4) ]
            f.readline() # skip line
            print "Case #%d: %s" % (Tcur, foo(args))

        f.close()

def foo(M):
    x = findWin(M, 'X')
    o = findWin(M, 'O')

    if x:
        return 'X won'
    if o:
        return 'O won'
    
    if any( any(c == '.' for c in r) for r in M ):
        return 'Game has not completed'
    
    return 'Draw'
    
def findWin(M, p):
    return scanHor(M, p) or scanVert(M, p) or scanDiag(M, p)

def scanHor(M, p):
    return any( all(c == p or c == 'T' for c in r) for r in M )

def scanVert(M, p):
    return any( all(r[i] == p or r[i] == 'T' for r in M) for i in range(4) )

def scanDiag(M, p):
    return all(M[i][i] == p or M[i][i] == 'T' for i in range(4)) or all(M[i][3-i] == p or M[i][3-i] == 'T' for i in range(4))

if __name__=="__main__":
    main()
