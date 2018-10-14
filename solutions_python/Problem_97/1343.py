#!/usr/bin/env python
"""
recycled_numbers.py

a script for the Google code jam 2012 Qulification Round Problem C

USAGE: python recycled_numbers.py filename.in filename.out
"""
import sys

RECYCLED = {}

def go(inputfile):
    result = []

    num_of_problems = int(inputfile.readline())
    
    for case in range(1,num_of_problems+1):
        problem = inputfile.readline()
        [a,b] = problem.split(' ')
        a = int(a)
        b = int(b)
        solution = solve(a,b)
        solution_str = 'Case #%i: %i\n' % (case, solution)
        result.append(solution_str)
                      
    return result

def solve(a, b):
    
    if b < 20: 
        return 0
    
    found = []
    
    for x in range(a,b+1):
        recycled = []
        recycled = recycle(x)
        #print "A/B:", a, "/", b, "X/recycled:", x, recycled
    
        if len(recycled) > 0:
            for r in recycled:
                if r <= b:
                    found.append(r);
    
    return len(found)

def recycle(num):
    if num in RECYCLED:
        return RECYCLED[num]
    
    num_str = str(num)
    recycled = []
    
    if len(num_str) == 1:
        return recycled
    
    for i in range(1, len(num_str)):
        new_num =  num_str[-i:] + num_str[:-i]
        if new_num[0] <> '0' and int(new_num) > num:
            if int(new_num) not in recycled:
                recycled.append(int(new_num))

    RECYCLED[num] = recycled

    return recycled

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print 'USAGE: python recycled_numbers.py filename.in filename.out'
        sys.exit(0)

    # translate the lines
    result = []
    inputfile = file(sys.argv[1], 'r')
    result = go(inputfile)
    inputfile.close()

    # write lines to outfile
    out = file(sys.argv[2], 'w')
    out.writelines(result)
    out.close()