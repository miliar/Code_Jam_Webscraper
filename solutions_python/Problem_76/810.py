#!/usr/bin/env python
import sys

class InputException(Exception):
    pass

def parse_file(filename):
    f = file(filename, 'r')
    case_num = int(f.readline())
    lines = f.readlines()
    if len(lines) != case_num * 2:
        raise InputException("bad input: case number mismatch")
    f.close()
    cases = []
    for i in xrange(0, len(lines), 2):
        num_candies = int(lines[i])
        candies = lines[i+1].split()
        if num_candies != len(candies):
            raise InputException("bad input: candies number mismatch", lines[i], lines[i+1])
        cases.append([int(candy) for candy in candies])
        
    return cases

def solve_case(sequence):
    patrick_sum = 0
    for candy in sequence:
        patrick_sum ^= candy
    
    if patrick_sum != 0:
        return None
    
    # else give smallest candy

    return sum(sorted(sequence)[1:])

def main():
    if len(sys.argv) != 3:
        print 'usage: %s <inputfile> <outputfile>' % sys.argv[0]
        return
    
    try:
        cases = parse_file(sys.argv[1])
    except InputException, e:
        print 'Got exception:', e
        return
    
    sys.stdout = file(sys.argv[2], 'w')
    
    for count in xrange(len(cases)):
        solution = solve_case(cases[count])
        if solution is None: 
            print 'Case #%d: NO' % (count + 1)
        else:
            print 'Case #%d: %d' % (count + 1, solution)
         
if __name__=='__main__':
    main()
