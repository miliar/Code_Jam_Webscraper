# -*- encoding: utf-8 -*-
##############################################################################
import sys
from math import sqrt
def cout_init(X,F,C,n):
    return C/(2 + n*F)
    
def cout(X,F,C,n):
    return X/(2 + n*F)

def cout_after(X,F,C,n):
    m=n+1
    return cout_init(X,F,C,n) + cout(X,F,C,m)

def get_time(line):
    line = line.split()
    C = float(line[0])
    F = float(line[1])
    X = float(line[2])
    print "C",C
    print "F",F
    print "X",X
    timer = 0.0
    n=0
    while cout(X,F,C,n) > cout_after(X,F,C,n):
        timer += cout_init(X,F,C,n)
        n =n+1
    timer +=cout(X,F,C,n)
    return timer

def process(i, fin, fout):
    line = fin.readline().strip('\n')
    res = get_time(line)
    fout.write("Case #%d: %s\n" % (i+1, res))

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
