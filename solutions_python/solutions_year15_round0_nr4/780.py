import sys

import numpy as np 


def whowins(case):
    X, R, C = [int(c) for c in case.split()]
    if R<C:
        R,C = C,R

    if X>6:             # hole constructable with single tile
        return "RICHARD"
    elif X>R and X>C:   # straight one doesnt fit
        return "RICHARD"
    elif X>R+C:         # L-shape doesnt fit
        return "RICHARD" 
    elif X/2>R or X/2>C:  #"squarred one" doesnt fit
        return "RICHARD"
    elif R*C % X != 0:      #cant fill all squares with X-tuple
        return "RICHARD"  
    elif 4==X and 4==R and 2==C:
        return "RICHARD"
    else:
        return "GABRIEL"


if "__main__" == __name__:
    
    print(sys.argv[1])
    inputfile = sys.argv[1]

    with open(inputfile, 'r') as f:
        T = int(f.readline())
        cases = []
        for _ in range(T):
            cases.append(f.readline())
    out = ""

    for i in range(T):
        out += "Case #{}: {}\n".format(i+1, whowins(cases[i]))

    with open("out_"+inputfile, 'w') as f:
        f.write(out)
    print(out)