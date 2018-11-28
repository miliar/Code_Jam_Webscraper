#!/usr/bin/env python
import sys

class InputException(Exception):
    pass

def parse_file(filename):
    f = file(filename, 'r')
    case_num = int(f.readline())
    lines = f.readlines()
    if len(lines) != case_num:
        raise InputException("bad input: case number mismatch")
    f.close()
    cases = []
    for i in xrange(0, len(lines)):
        elements = lines[i].split()
        if len(elements) != 3:
            raise InputException
        cases.append([int(element) for element in elements])
        
    return cases

def solve_case(n, pd, pg):
    for d in xrange(1, n+1):
        if (pd * d) % 100 == 0:
            dw = (pd * d) / 100
            for o in xrange(0, n * 100 * 100 + 1):
                if (pg * (o + d)) % 100 == 0 and (pg * (o + d)) / 100 - dw >= 0 and (pg * (o + d)) / 100 - dw <=o:
                    return True
    return False

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
        if solve_case(*cases[count]):
            print 'Case #%d: Possible' % (count + 1)
        else:
            print 'Case #%d: Broken' % (count + 1)
         
if __name__=='__main__':
    main()
