import sys
import os
import math

def decode(line1, lin2):
    """decoder"""
    mul = lambda a,b : a*b
    num_entered, num_total = tuple(int(i) for i in line1.split())
    prob = list(float(i) for i in lin2.split())
    score_1 = (num_total - num_entered + 1) * reduce(mul, prob[:num_entered],1) + (2* num_total - num_entered + 2) * (1 - reduce(mul, prob[:num_entered],1))
    def backtrack(i):
        return reduce(mul, prob[:num_entered - i], 1) * (num_total - num_entered + 1 + 2*i) + (1 - reduce(mul, prob[:num_entered - i], 1)) * (num_total - num_entered + 1 + 2*i + num_total + 1)
    score_intrium = list(backtrack(i) for i in range(num_entered+1))
    score_shabi = 2 + num_total
    return min(min(score_intrium), score_shabi)

def main(f_path):
    """main"""
    file_object = open(f_path, 'r')
    
    num_cases = int(file_object.readline())
    for i in range(num_cases):
        line1, line2 = file_object.readline(), file_object.readline()
        print 'Case #%i: %f' % (i+1, decode(line1, line2))

if __name__ == '__main__':
    if (len(sys.argv) == 2):
        main(sys.argv[1])
        

        

            
