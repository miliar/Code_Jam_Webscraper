#!/usr/bin/python -tt
"""
"""

import sys
import math
import time


def prob(problem, input_type):
   
    # boilerplate to handle code jam specific input files

    problem = problem
    input_type = input_type

    if input_type == '':
        filestring = problem + '_'
    else:
        filestring = problem + '_' + input_type + '_'

    finput = open(filestring + 'input.txt', 'r')
    foutput = open(filestring + 'output.txt', 'w')

    # store input file lines in list
    inputs = finput.readlines()
    print(inputs)

    # input file parser
    index = 0
    num_testcases = int(inputs[index]) 
    lines_per_testcase = 1
    print('number testcases:', num_testcases)
    index += 1


    for testcase in range(1,num_testcases+1):
        print('testcase:', testcase)

        # grab input data
        lawndim = (inputs[index].split())
        lawndim = [int(i) for i in lawndim]
        n,m = lawndim[0], lawndim[1]
        lines_per_testcase = lawndim[0] 
        index += 1
        print(n,m)
        
        height=[]
        for row in range(n):
            row_values = inputs[index+row].split()
            row_values = [int(i) for i in row_values]
            print(row_values)
            height.append(row_values)
        print(height)
        
        # implement solution algorithm
        # pattern is valid if each square's height entry
        # satisfies being the max of either the row
        # or col in which it resides

        # calculate max in each row/col
        row_max = []
        col_max = []
        for row in range(n):
            max = 0
            for col in range(m):
                if height[row][col] > max:
                    max = height[row][col]
            row_max.append(max)

        for col in range(m):
            max = 0
            for row in range(n):
                if height[row][col] > max:
                    max = height[row][col]
            col_max.append(max)

        print(row_max,col_max)

        # check if each entry meets valid pattern criteria
        output = 'YES'
        for row in range(n):
            for col in range(m):
                if (height[row][col] >= row_max[row] or  
                    height[row][col] >= col_max[col] ):
                       continue
                else:
                    output = 'NO'
                    break
            if output == 'NO':
                break
                
        print(output)
        foutput.write('Case #%d: %s\n' % (testcase, output))
       
        # end of solution algorithm

        index = index + lines_per_testcase 
    
    finput.close()
    foutput.close()

# main() handles cmdline parsing and runtime check 
def main():

  # Omit the [0] element which is the script itself.
  args = sys.argv[1:]

  if not args:
    print('usage: [--problem] <problem> [--input] (sample|small|large)')
    sys.exit(1)

  if not args[3]:
      args[3] = ''

  s = time.time()
  
  answer = prob(args[1], args[3]) 

  print('Runtime: %0.2f seconds' % (time.time() - s))

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
