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
        n, l, h = [int(x) for x in lines[i].split()]
        i+=1
        walls = []
        notes = [int(x) for x in lines[i].split()]
        if len(notes) != n: 
            raise Exception('bah', ws, we)
        i += 1
        
        cases.append((l, h, notes))
        
    return cases

def gcd(num1, num2):
    if num1 > num2:
        for i in range(1,num2+1):
            if num2 % i == 0:
                if num1 % i == 0:
                    result = i
        return result

    elif num2 > num1:
        for i in range(1,num1+1):
            if num1 % i == 0:
                if num2 % i == 0:
                    result = i
        return result

    else:
        result = num1*num2/num1
        return result

def mgcd(numbers):
    if len(numbers) == 0:
        return 1
    if len(numbers) == 1:
        return number
    
    cur_gcd = gcd(numbers[0], numbers[1])
    for i in xrange(2, len(numbers)):
        cur_gcd = gcd(cur_gcd, numbers[i])
    
    return cur_gcd

# the function to calculate the LCM
def lcm(num1, num2):
    result = num1*num2/gcd(num1,num2)
    return result

def solve_case(l, h, notes):
#    gcd = mgcd(notes) 
#    if  gcd >= l:
#        return gcd
#    
#    #lcm
#    lcm = numpy.product(notes)/gcd
#    if lcm <= h:
#        return lcm
        
    for i in xrange(l, h+1):
        good_note = True
        for note in notes:
            if not (note % i == 0 or i % note == 0):
                good_note = False
                break
        if good_note: return i 
    
    return 
        

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
        print 'Case #%d:' % (count + 1), 
        note = solve_case(*cases[count])
        if note is None:
            print 'NO'
        else:
            print note 
                
         
if __name__=='__main__':
    main()
