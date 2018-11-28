#!/usr/bin/python -tt
"""
"""

import sys
import math
import time


def prob(problem, input_type):
   
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
        #print('testcase:', testcase)

        # grab input data
        # implement solution algorithm
        args = inputs[index].replace('\n','').split()
        r = int(args[0])
        t = int(args[1])

        print(r,t)
        
        # area of n rings = 2r*n + [1 + 5 + 9 + 13 + ...]
        # = 2rn + [1 + 3 + 5 + 7 + ...] + [2 + 4 + 6 + 8 + ...]
        # = 2rn + n^2 + n*(n-1)

        numrings = math.floor((-(2*r-1)+math.sqrt((2*r-1)**2+8*t))/4) 
        #numrings = (-(2*r-1)+math.sqrt((2*r-1)**2+8*t))/4 
        
        print('Case #%d: %d\n' % (testcase, numrings))
        foutput.write('Case #%d: %d\n' % (testcase, numrings))
       
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
