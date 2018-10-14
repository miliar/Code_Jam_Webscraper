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
        testcase_inputs = inputs[index].replace('\n','').split() 
        testcase_inputs = [float(i) for i in testcase_inputs]
        print(testcase_inputs)
        
        rate = 2.0
        farm_cost = testcase_inputs[0]
        speedup = testcase_inputs[1]
        goal = testcase_inputs[2]

        # implement solution algorithm
        
        time1 = goal/rate
        time2 = farm_cost/rate + goal/(speedup + rate)

        while (time1 - time2 > 0.0):
            rate += speedup
            time1 = time2
            time2 = time2 - goal/rate + farm_cost/rate + goal/(speedup + rate)
            
        print('Case #%d: %0.7f' % (testcase, time1))
        foutput.write('Case #%d: ' % (testcase))
        foutput.write(str(time1))
        foutput.write('\n')

        # end of solution algorithmi
        
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
