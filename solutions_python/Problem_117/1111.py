import os
import numpy as np
import argparse

def run(filename, out_filename):


    f = open(filename, 'r')
    f_out = open(out_filename, 'w')    
    
    no_of_cases = int(f.readline())
    print 'Number of cases: ', no_of_cases

    lines = f.readlines()
    case = 1
    case_l_nr = 0

    for line in lines:
        line = line.replace('\n', '')
        if case_l_nr == 0:
            [N,M] = line.split(' ')
            N = int(N)
            M = int(M)
            lawn = np.zeros((N, M)) 
            case_l_nr +=1
        
        else:
            lawn[case_l_nr-1][:] = np.asarray(line.split(' '))
            if case_l_nr == N:

                status = evaluate(lawn)
                message = 'Case #%i: %s\n'% (case,status)
                print message
                f_out.write(message) 

                case +=1
                case_l_nr = 0
            else:
                case_l_nr += 1

def evaluate(lawn):
    '''
    Evaluate current lawn, given as numpy ndarray.

    To be possible to adapt the lawn, the element of the lawn has to be 
    maximum of the lown eather in row or in column. 
    ''' 

    [N, M] = lawn.shape
    ver_max = lawn.max(axis=0)
    ver_max_fullsize = np.tile(ver_max, (N,1)) 
    hor_max = lawn.max(axis=1)
    hor_max_fullsize = np.tile(hor_max,  (M,1)).T
   
    # check if possible to create. If there is single False, than the lawn can
    # not be created.
    check_result = ((lawn == hor_max_fullsize ) |  (lawn  == ver_max_fullsize))

    if check_result.min() == False:
        return 'NO'

    else:
        return 'YES'


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
