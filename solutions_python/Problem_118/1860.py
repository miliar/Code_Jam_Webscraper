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

    def ispalindrome(number):
        numstr = str(number)
        for i in range(len(numstr)//2+1):
            if numstr[i] == numstr[len(numstr)-1-i]:
                continue
            else:
                return False
        else:
            return True

    def fair_square(number):
        #print('fair_square',number,math.sqrt(number))
        if ispalindrome(number):
            if math.sqrt(number) % 1 == 0:
               if ispalindrome(round(math.sqrt(number))): 
                  return True
               else:
                   return False
            else:
                return False
        else:
            return False

    #print('121',ispalindrome(121))
    #print('6',ispalindrome(6))
    #print('12',ispalindrome(12))
    #print('1112111',ispalindrome(1112111))
    #print('11122111',ispalindrome(11122111))
    #print('1',ispalindrome(1))
    #print('9',ispalindrome(9))
    #print('121',ispalindrome(121))

    #print('1',fair_square(1))
    #print('4',fair_square(1))
    #print('9',fair_square(9))
    #print('121',fair_square(121))
    #print('16',fair_square(16))
    #print('22',fair_square(22))
    #print('676',fair_square(676))

    for testcase in range(1,num_testcases+1):
        print('testcase:', testcase)

        # grab input data
        bounds = inputs[index].split()
        low, high = int(bounds[0]), int(bounds[1])
        print(low,high)

        # implement solution algorithm
        count = 0
        for i in range(low,high+1):
            if ispalindrome(i):
              if math.sqrt(i) % 1 == 0:
                 if ispalindrome(round(math.sqrt(i))):
                     print('found fair_square_num:', i)
                     count += 1
        print(low,high+1)

        output = count
        print(count)
        foutput.write('Case #%d: %d\n' % (testcase, count))
       
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
