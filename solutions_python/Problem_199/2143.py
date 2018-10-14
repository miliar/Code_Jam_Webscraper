import numpy as np
import sys

sys.setrecursionlimit(100000)

def flip_beginning(state, size):
    new_state = ""
    for char in state[:size]:
        if char == "+":
            new_state += "-"
        else:
            new_state += "+"
    new_state += state[size:]
    return new_state

def min_transform_cost(state,size):
    if len(state) == size:
        if state == "+"*size:
            return 0
        elif state == "-"*size:
            return 1
        else:
            return np.inf
    
    if len(state) < size:
        if state == "+"*len(state):
            return 0
        else:
            return np.inf
        
    first_minus_index = state.find("-")
    if first_minus_index == -1:
        return 0

    if len(state[first_minus_index:]) < size:
        return np.inf

    subproblem = flip_beginning(state[first_minus_index:],size)
    cost = min_transform_cost(subproblem,size) + 1

    return cost

f = open('A-large.in', 'r')
output = open("out.txt", 'w')

first_line = f.readline()
for index, line in enumerate(f):
    line = line.strip()
    line = line.split(" ")
    
    state = line[0]
    size = line[1]

    cost = min_transform_cost(state,int(size))
    if cost == np.inf:
        string = "Case #" + str(index+1) + ": IMPOSSIBLE"
    else:
        string = "Case #" + str(index+1) + ": " + str(cost)
        
    output.write(string + "\n")

f.close()
output.close()