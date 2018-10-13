'''
CodeJam Practice 
Created on 2012-12-20

@author: festony
'''

from cj_lib import *
from properties import *

import math
import fractions


curr_file_name = 'A-large'
#curr_file_name = 'A-small-attempt0'
#curr_file_name = 'test'

# map(int, input_lines.pop(0).split(' '))

def input_dividing_func(input_lines):
    total_case = int(input_lines.pop(0))
    case_inputs = []
    for i in range(total_case):
        N, X = map(int, input_lines.pop(0).split(' '))
        F = map(int, input_lines.pop(0).split(' '))
        case_inputs.append([N, X, F])
    return case_inputs
    
def process_func(func_input):
    N, X, F = func_input
    SF = sorted(F)
    D = []
    i = len(SF) - 1
    while True:
        #print '-', SF
        if SF == []:
            break
        if i < 0:
            break
        s = SF.pop(0)
        if SF == []:
            D.append(s)
            break
        if i > len(SF) - 1:
            i = len(SF) - 1
        i = len(SF) - 1
        while SF[i] + s > X and i > 0:
            i -= 1
        if SF[i] + s > X:
            D.append(s)
            break
        l = SF.pop(i)
        D.append(l + s)
        i -= 1
        #print SF,
        #print D
    #print 'f',SF,D
    return len(SF) + len(D)

run_proc(process_func, input_dividing_func, curr_working_folder, curr_file_name)


