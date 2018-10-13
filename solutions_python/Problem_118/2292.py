# -*- encoding: utf-8 -*-
##############################################################################
import sys
from math import sqrt

def is_reversible(N):
    lrN = [x for x in str(N)]
    rlN = lrN[:]
    rlN.reverse()
    return lrN == rlN

def is_square(n):
    return sqrt(n).is_integer()

def first_fair_square(Aa):
    while not (is_reversible(Aa) and is_square(Aa) and is_reversible(int(sqrt(Aa))) ):
        Aa+=1
    return Aa

def fair_squares(line):
    line = line.split()
    A = int(line[0])
    B = int(line[1])
    count = 0
    ffsrP = first_fair_square(A)
    while ffsrP <= B:
        count += 1
        ffsrP += 1
        ffsrP = first_fair_square(ffsrP)
    return count

def process(i, fin, fout):
    line = fin.readline().strip('\n')
    res = fair_squares(line)
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
