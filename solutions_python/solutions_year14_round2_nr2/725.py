from __future__ import print_function
import argparse

parser = argparse.ArgumentParser(description='Code Jam File Input handler')
parser.add_argument('file_name', metavar='file_name', type=str, help='File name to use as input')

def getAnswer( a, b, k ):
    return sum( (i&j)< k for i in xrange(a) for j in xrange(b) )
            
def solve( file_name ):
    with open(file_name,'r') as fh, open(file_name + '_solution.out', 'w') as fo:
        num_cases = int( fh.readline() )
        for case in xrange(num_cases):
            a,b,k =  map(int, map(float, fh.readline().split() ) )
            print( 'Case #%d: %d'%( case + 1, getAnswer( a,b,k) ),file=fo )

solve( parser.parse_args().file_name )
