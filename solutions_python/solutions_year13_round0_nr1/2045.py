import sys
import numpy as np

def get_state(field):
    X = (field == 1) | (field == 3)
    O = (field == 2) | (field == 3)
    for i in range(4):
        if np.all(X[i,:]) or np.all(X[:,i]):
            return "X won"
        if np.all(O[i,:]) or np.all(O[:,i]):
            return "O won"
    if np.all(X.diagonal()) or np.all(np.fliplr(X).diagonal()):
        return "X won"
    if np.all(O.diagonal()) or np.all(np.fliplr(O).diagonal()):
        return "O won"
    if np.all(X | O):
        return "Draw"
    return "Game has not completed"

with open(sys.argv[1],'r') as f:
    lines = f.readlines()

num_cases = int(lines[0])

for case in range(num_cases):
    field = np.zeros((4,4),int)
    for i,line in enumerate(lines[case*5+1:case*5+6]):
        for j,char in enumerate(line):
            if char == 'X':
                field[i,j] = 1
            elif char == 'O':
                field[i,j] = 2
            elif char == 'T':
                field[i,j] = 3
    state = get_state(field)
    print "Case #%s: %s"%(case+1, state)
