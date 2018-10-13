import sys

import math


def solve(C,F,X):
    seuil = max(0,math.ceil((F*X-F*C-2*C)/(F*C)))
    solution = sum ([ C/(2+i*F) for i in range(int(seuil)) ]) + X/(2+seuil*F)
    
    return solution
 


file = open(sys.argv[1])
file.readline()

for i,l in enumerate(file.readlines()):
  lspl = [float(x) for x in l.split()]
  
  print "Case #%i: %.8f"%(i+1, solve(lspl[0], lspl[1], lspl[2]))


    