import os
import numpy as np
import argparse
from math import *

def run(filename, out_filename):


    f = open(filename, 'r')
    f_out = open(out_filename, 'w')    
    
    no_of_cases = int(f.readline())
    print 'Number of cases: ', no_of_cases

    case = 1
    lines = f.readlines()

    for line in lines:
        line = line.replace('\n', '')
        [low, high] = line.split(' ')
        print low, high
        status = fairAndSquare(int(low), int(high))

        message = 'Case #%i: %s\n'% (case,status)
        print message
        f_out.write(message) 

        case += 1

def fairAndSquare(low, high):
    '''
    ''' 

    low_sqrt = int(ceil(sqrt(low)))
    high_sqrt = int(floor(sqrt(high)))

    list_of_fair_and_square = []
    for i in xrange(low_sqrt, high_sqrt+1):
        status = checkFair(str(i))
        if status is True:
            status = checkFair(str(i**2))
            if status is True:  
                list_of_fair_and_square = list_of_fair_and_square + [str(i**2)]
    return len(list_of_fair_and_square)

def checkFair(text):

    #print 'text', text
    if len(text) == 1:
        return True
    else:
        if text[0] == text[-1]:
            if len(text) == 2:
                return True
            else:
                return checkFair(text[1:-1])

        else:
            return False

    


if __name__ == '__main__': 

    parser = argparse.ArgumentParser(description='Lawn')

    parser.add_argument('-i','--input-file',                                        
                             action="store", help='Input filename')
    parser.add_argument('-o', '--output-file',
                             action ='store', help='Output file')
    args = parser.parse_args()
    
    if args.input_file == None:
        args.input_file = 'input.txt'    
    if args.output_file == None:
        args.output_file = 'output.txt'
    run(args.input_file, args.output_file)    
