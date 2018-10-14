__author__ = 'isira'

import math
import os

dir = '/Users/isira/Documents/cpp/'

fName = { 0 : 'test' , 1: 'small' , 2 : 'large' }
run = 2
input_file = '{}/{}.in'.format( dir , fName[run])
output_file = '{}/{}.out'.format( dir , fName[run])

if os.path.exists(output_file):
    os.remove(output_file)


def cruise( list , D ):
    # Find the one which takes most time
    l = []
    m = -1
    for i,j in list:
       s = ( D - i )/j
       m = max( s , m)



    return D/m





def main():
    with open( input_file) as f_in:
        t = int(f_in.readline())
        for i in range(1, t + 1):
            D, N = map( int , f_in.readline().strip().split(' '))
            lines = []
            for j in range( 0 ,N ):
                K, M = list( map(int, f_in.readline().strip().split(' ') ))
                lines.append([ K, M])
            with open( output_file , 'a+') as f_out:
                print('Case #{}: {}'.format(i, cruise( lines, D ) ) ,  file= f_out)


if __name__ == '__main__':
    main()