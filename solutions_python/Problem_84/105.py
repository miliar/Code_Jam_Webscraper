#!/usr/bin/env python
import sys
import numpy

class InputException(Exception):
    pass

def parse_file(filename):
    f = file(filename, 'r')
    case_num = int(f.readline())
    lines = f.readlines()
    f.close()
    cases = []
    i = 0
    while i < len(lines):
        r, c = [int(x) for x in lines[i].split()]
        i+=1
        picture = []
        row = 0
        while row < r:
            picture.append(lines[i].strip()) 
            if len(picture[-1]) != c:
                raise Exception('blah', r, c, picture)
            i += 1
            row += 1
        
        cases.append((r, c, picture))
        
    return cases

def is_possible(r, c, picture):
    for i in xrange(r):
        streak = 0
        for j in xrange(c):
            if picture[i][j] == '.':
                if streak % 2 != 0:
                    return False
                streak = 0
            else:
                streak += 1
        if streak % 2 != 0:
            return False
        
    for j in xrange(c):
        streak = 0
        for i in xrange(r):
            if picture[i][j] == '.':
                if streak % 2 != 0:
                    return False
                streak = 0
            else:
                streak += 1
        if streak % 2 != 0:
            return False
    
    return True

def solve_case(r, c, picture):
    if not is_possible(r, c, picture):
        return
    
    for i in xrange(r):
        for j in xrange(c):
            if picture[i][j] == '#':
                picture[i] = picture[i][:j] + '/\\' + picture[i][j+2:]
                picture[i+1] = picture[i+1][:j] + '\/' + picture[i+1][j+2:]
                
    return picture

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
        print 'Case #%d:' % (count + 1)
        picture = solve_case(*cases[count])
        if picture is None:
            print 'Impossible'
        else:
            for row in picture:
                print row
                
         
if __name__=='__main__':
    main()
