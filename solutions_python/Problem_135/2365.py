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
    lines_per_testcase = 10 
    print('number testcases:', num_testcases)
    index += 1


    for testcase in range(1,num_testcases+1):
        print('testcase:', testcase)

        # grab input data
        row1 = int(inputs[index])
        row2 = int(inputs[index+5])
        cards1 = inputs[index+row1].replace('\n','').split() 
        cards2 = inputs[index+5+row2].replace('\n','').split() 
        cards1 = [int(i) for i in cards1]
        cards2 = [int(i) for i in cards2]
        print(row1, row2, cards1, cards2)

        # implement solution algorithm
           
        print('Case #%d: ' % (testcase), end='')
        foutput.write('Case #%d: ' % (testcase))
        if len(set(cards1+cards2)) == 8:
           print('Volunteer cheated!')
           foutput.write('Volunteer cheated!\n')
        elif len(set(cards1+cards2)) <= 6:
           print('Bad magician!')
           foutput.write('Bad magician!\n')
        else:
           for i in range(0,4):
               if cards1[i] in cards2: 
                   print(str(cards1[i]))
                   foutput.write(str(cards1[i]))
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
