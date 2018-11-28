from __future__ import print_function
import argparse

parser = argparse.ArgumentParser(description='Code Jam File Input handler')
parser.add_argument('file_name', metavar='file_name', type=str, help='File name to use as input')

def solve( file_name ):
    with open(file_name,'r') as fh, open(file_name + '_solution.out', 'w') as fo:
        num_cases = int( fh.readline() )
        for case in xrange(num_cases):
            a1 = int( fh.readline() )
            data,data2 = [],[]
            for row in range(4):
                data.append( map( int, fh.readline().split() ) )
            set1 = set( data[ a1-1 ] )
            a2 = int( fh.readline() )
            for row in range(4):
                data2.append( map(int, fh.readline().split() ) )
            set2 = set( data2[a2-1] )
            answer = set1.intersection(set2)
            if len( answer) == 0:
                result = 'Volunteer cheated!'
            elif len( answer ) > 1:
                result = 'Bad magician!'
            else:
                result = str( answer.pop() )
            print('Case #%d: %s'%(case+1, result),file=fo )

solve( parser.parse_args().file_name )
