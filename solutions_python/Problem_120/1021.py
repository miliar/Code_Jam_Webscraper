import sys
from functools import reduce
import operator
import numpy as np

input_file = open(sys.argv[1], 'r')
output_file = open("out_" + sys.argv[0].rstrip(".py"), 'w')

input_size = int(input_file.readline().rstrip("\n"))



case = 1
for i in range(input_size):
    breaked= False
    (r, t) = map(int, input_file.readline().rstrip("\n").split(" "))
    current_radius = r
    nbBlackRing = 0
    used = 0
    while(t >= 0):
        t = t - (current_radius*2 + 1)
        nbBlackRing+=1
        current_radius += 2
    nbBlackRing-=1
    output_file.write("Case #" + str(case) + ": " + str(nbBlackRing) + "\n")
    print("Case #" + str(case) + ": " + str(nbBlackRing) + "\n")
    case +=1

        
    
