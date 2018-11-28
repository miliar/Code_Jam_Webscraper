import sys
from numpy import *
from functools import reduce
import operator
import numpy as np
input_file = open(sys.argv[1], 'r')
output_file = open("out_" + sys.argv[0].rstrip("."), 'w')

input_size = int(input_file.readline().rstrip("\n"))


def is_fair_square(integer):
    if (list(str(integer)) == list(str(integer))[::-1]):
        square = np.sqrt(integer)
        
        square_int = int(square)

        if(square_int != square):
            return False

        return list(str(square_int)) == list(str(square_int))[::-1]

case = 1
for i in range(input_size):
    (minimum,maximum) = map(int, input_file.readline().rstrip("\n").split(" "))
    result = 0
    for j in range(minimum, maximum + 1):
        if is_fair_square(j):
            result+= 1
    output_file.write("Case #" + str(case) + ": " + str(result) + "\n") 
    case +=1
