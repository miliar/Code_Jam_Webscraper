'''
Created on Apr 13, 2013

@author: nils
'''
import sys
import numpy
from ttt import *

def main():
    work_file(sys.argv[1], sys.argv[2])


def work_file(fin, fout):
    print("Working now")
    with open(fin) as in_, open(fout, 'w') as out_:
        num_test = (int(in_.readline().strip()))
        for i in range(num_test):
            array_list = []
            for _ in range(4):
                line = in_.readline().strip()
                array_list.append(list(line))
            
            in_.readline()
              
            game = numpy.array(array_list)
            solution = solve(game)
            
            if solution == X:
                out_sol = 'X won'
            elif solution == O:
                out_sol = 'O won'
            elif solution == DRAW:
                out_sol = 'Draw'
            else:
                out_sol = 'Game has not completed'
                
            out_.write('Case #%d: %s\n' % (i + 1, out_sol))

if __name__ == '__main__':
    main()