'''
Created on Apr 11, 2014

@author: stephaniedong
'''
from io import StringIO
import numpy as np
import os


def skip_rows(f, num_rows):
    """
    file, int -> NoneType

    Effect: skips over next num_rows rows in file

    >>> test_file = StringIO('row1\\n row2\\n row3\\n row4\\n')
    >>> skip_rows(test_file, 3)
    >>> test_file.readline()
    ' row4\\n'
    """
    for row in range(num_rows):
        f.readline()




def read_input_file(inf, num_rows):
    """
    file, int -> listof(int)
    
    Effect: reads and stores a file as ???
    
    
    """
    
    skip_rows(inf, num_rows)
    
    string_data =[[int(str) for str in line.split()]for line in inf if line.strip()!='']
    
    return string_data


    
def the_master_plan(inf, num_rows, outf):
    
    data = read_input_file(inf, num_rows)
    casenum=1
    
    total_cases = data[0][0]
    del data[0]
    
    while(total_cases!=0):
        deal_with_one_set(data,casenum,outf)
        total_cases = total_cases - 1  
        casenum =casenum + 1      



def deal_with_one_set(data,casenum,ouf):
    
    first_answer = data[0][0]
    first_set = [data[1],data[2],data[3],data[4]]
    second_answer = data[5][0]
    second_set = [data[6],data[7],data[8],data[9]]
    del data[0:10]
    
    determine_results(first_answer,first_set,second_answer,second_set, casenum, outf)
    
    
    
def determine_results(first_answer,first_set,second_answer,second_set, casenum, outf):
    
    first_row = first_set[first_answer-1]
    second_row= second_set[second_answer-1]

    intersection = [num for num in first_row if num in second_row]
    
    print_results(intersection, casenum,outf)
    


def print_results(result, casenum,outf):
    
    if (len(result) == 0):
        result_message="Volunteer cheated!"
    elif(len(result) == 1):
        result_message= str(result[0])
    else:
        result_message= "Bad magician!"
        
    
    outstring= "Case #"+str(casenum)+": "+result_message+"\n"
    
    outf.write(outstring)
















if __name__=='__main__':
    import doctest
    EPS = 1.0e-9
    print(doctest.testmod(verbose=False))
    
    import os
    os.chdir('/Users/stephaniedong/Documents/Eclipse Workspace/Google Code Jam A/src')     # modify with path to your src folder
    