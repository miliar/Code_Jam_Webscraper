import sys
import os
import math

def decode(line):
    """decoder"""
    out = 0
    line = line.split()
    min = int(line[0])
    max = int(line[1])
    
    num_digits = int(math.floor(math.log10(min))+1)
    
    check = {}
    for i in range(min, max+1):
        
        
        for j in range(1, num_digits):
            counter_part = (i%(10**j))*10**(num_digits - j) + i/(10**j)
            if (counter_part > i and counter_part >= min and counter_part <= max and (i,counter_part) not in check):
                out += 1
                check[(i,counter_part)] = True
                # print 'for n %i there is m %i' % (i, counter_part)
    return out

def main(f_path):
    """main"""
    file_object = open(f_path, 'r')
    
    num_cases = int(file_object.readline())
    for i in range(num_cases):
        line = file_object.readline()
        print 'Case #%i: %i' % (i+1, decode(line))

if __name__ == '__main__':
    if (len(sys.argv) == 2):
        main(sys.argv[1])
        

        

            
