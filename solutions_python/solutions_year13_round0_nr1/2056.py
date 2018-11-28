# -*- encoding: utf-8 -*-
##############################################################################
import sys

def process(num, fin, fout):
    square = [x for x in fin.read(20) if x!='\n']
    r1 = square[:4]
    r2 = square[4:8]
    r3 = square[8:12]
    r4 = square[12:16]
    c1 = [ square[i+0] for i in [0,4,8,12] ]
    c2 = [ square[i+1] for i in [0,4,8,12] ]
    c3 = [ square[i+2] for i in [0,4,8,12] ]
    c4 = [ square[i+3] for i in [0,4,8,12] ]
    d1 = [ square[i] for i in [0,5,10,15] ]
    d2 = [ square[i] for i in [3,6,9,12] ]
    
    X = [ len([x for x in y if x=='X' or x=='T']) for y in [r1, r2, r3, r4, c1, c2, c3, c4, d1, d2]]
    O = [ len([x for x in y if x=='O' or x=='T']) for y in [r1, r2, r3, r4, c1, c2, c3, c4, d1, d2]]
    nP = len([x for x in square if x=='.'])
    
    if 4 in X:
        s = "X won"
    elif 4 in O:
        s = "O won"
    elif nP == 0:
        s = "Draw"
    else:
        s = "Game has not completed"
    fin.readline()
    fout.write("Case #%d: %s\n" % (num+1, s))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "Please indicate input and output"
    fin = open(sys.argv[1], 'r')
    fout = open(sys.argv[2], 'w')
    N = int(fin.readline())
    for e in xrange(N):
        process(e, fin, fout)
    fin.close()
    fout.close()
    print " *** Done ***"

##############################################################################
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
