#!/usr/bin/env python3

import sys
from numpy import *

input_file = open(sys.argv[1], 'r')
output_file = open("out_" + sys.argv[0].rstrip("."), 'w')

input_size = int(input_file.readline().rstrip("\n"))

state = []

    


def analyse():
    got_point = False
    for i in range(4):
        ans = line_analyse(i, False)
        if ans == 'point':
            got_point = True
        elif ans:
            return ans
        ans = line_analyse(i, True)
        if ans == 'point':
            got_point = True
        elif ans:
            return ans
    ans = diagonal_analyse()
    print(ans)
    if ans:
        return ans
    if(got_point):
        return "not completed"
    else:
        return "draw"

def diagonal_analyse():
    temp_state = array(state)
    s = temp_state.diagonal()
    if ('.' not in s):
        if ((s[0] == s[1] == s[2] == s[3])         or
            (s[1] == 'T' and s[0] == s[2] == s[3]) or
            (s[2] == 'T' and s[0] == s[1] == s[3]) or
            (s[3] == 'T' and s[0] == s[1] == s[2])):
        
            return s[0]
    
        elif (s[0] == 'T' and s[1] == s[2] == s[3]):
            return s[1]
        
    temp_state = swapaxes(temp_state, 0,1)
    temp_state = temp_state[::-1]
    print (temp_state)
    s = temp_state.diagonal()
    if ('.' not in s):
        
        if ((s[0] == s[1] == s[2] == s[3])         or
            (s[1] == 'T' and s[0] == s[2] == s[3]) or
            (s[2] == 'T' and s[0] == s[1] == s[3]) or
            (s[3] == 'T' and s[0] == s[1] == s[2])):
        
            return s[0]
            
    elif (s[0] == 'T' and s[1] == s[2] == s[3]):
        return s[1]
    else:
        return False

def line_analyse(index, horizontal):
    if(horizontal):
        s = state[index]
    else:
        temp_state = array(state).transpose()
        s = temp_state[index]

    if ('.' in s):
        return "point"
    
    if ((s[0] == s[1] == s[2] == s[3])         or
        (s[1] == 'T' and s[0] == s[2] == s[3]) or
        (s[2] == 'T' and s[0] == s[1] == s[3]) or
        (s[3] == 'T' and s[0] == s[1] == s[2])):
        
        return s[0]
    
    elif (s[0] == 'T' and s[1] == s[2] == s[3]):
        return s[1]
    else:
        return False
        


for i in range(input_size):
    for j in range(4):
        state.append(list(input_file.readline().rstrip("\n")))
    ans = analyse()
    output_file.write("Case #" + str(i + 1) + ': ')
    if (ans == "draw"):
        output_file.write("Draw\n")
    elif (ans == "not completed"):
        output_file.write("Game has not completed\n")
    else:
        output_file.write(ans + " won\n")
                          
                          
    input_file.readline()
    state = []
