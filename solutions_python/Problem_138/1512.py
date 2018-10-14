from __future__ import print_function
import argparse

parser = argparse.ArgumentParser(description='Code Jam File Input handler')
parser.add_argument('file_name', metavar='file_name', type=str, help='File name to use as input')

def find_largest_greater_than( sorted_lst, val ):
    for pos, v in enumerate(sorted_lst):
        if v > val:
            return pos
    return 0

def getAnswer( naomi, ken ):
    return '%d %d'%(getDeceitScore(naomi, ken), getDefaultAnswer( naomi, ken))

def getDeceitScore(naomi, ken):
    if not naomi:
        return 0
    ns = sorted(naomi)
    ks = sorted(ken)
    score = 0
    while ns:
        if ns[0] > ks[0]:
            ns.pop(0)
            ks.pop(0)
            score+=1
        else:
            pos = None
            for pos, (i,j) in enumerate( zip( list(reversed(ns[1:])), list(reversed(ks[1:])))):
                if i <= j:
                    break
            if pos is None:
                ns.pop(0)
                ks.pop(0)
            else:
                ns.pop(0)
                ks.pop( len(ns) - pos)
    return score
            

def getDefaultAnswer( naomi, ken):
    ns = sorted( naomi)
    ks = sorted( ken )
    score = 0
    while ns:
        val = ns.pop(-1)
        if val > ks[-1]:
            kval = ks.pop(0)
            score +=1
        else:
            pos = find_largest_greater_than( ks, val)
            ks.pop(pos)
    return score



def solve( file_name ):
    with open(file_name,'r') as fh, open(file_name + '_solution.out', 'w') as fo:
        num_cases = int( fh.readline() )
        for case in xrange(num_cases):
            nums =  int( fh.readline() )
            naomi = map( float, fh.readline().split() )
            ken   = map( float, fh.readline().split() )
            print( 'Case #%d: %s'%( case + 1, getAnswer( naomi, ken ) ),file=fo )

solve( parser.parse_args().file_name )
