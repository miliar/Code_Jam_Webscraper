from sys import argv
from itertools import izip, imap, count, combinations, permutations
import math

def replace( pic, x, y ):
    try:
        ok = ( pic[x][y] == "#" and pic[x][y+1] == "#" and pic[x+1][y] == "#" and pic[x+1][y+1] == "#" )
    except IndexError:
        return False
    if not ok:
        return False
    pic[x][y] = "/"
    pic[x][y+1] = "\\"
    pic[x+1][y] = "\\"
    pic[x+1][y+1] = "/"
    return True

def solvecase( R, C, pic ):
    for rown in xrange(R):
        for coln in xrange(C):
            if pic[rown][coln] == "#" :
                ok = replace( pic, rown, coln )
                if not ok:
                    return False
    return True

def main():
    global inf
    inf = argv[1]
    inf = open(argv[1])
    ncase = int(inf.readline().strip())
    for case in xrange(1, ncase+1):
        #print "input", case
        RC = inf.readline().strip()
        #print CD
        R, C = map(int, RC.split())
        pic = []
        for i in xrange(R):
            row = inf.readline().strip()
            #print PV
            row = list(row)
            pic.append( row )
        ans = solvecase( R, C, pic )
        print "Case #{n}:".format( n=case )
        if not ans:
            print "Impossible"
        else :
            for row in pic:
                print "".join(row)
    return 0

main()

