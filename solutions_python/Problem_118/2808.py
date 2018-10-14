#! -*- Encoding: Latin-1 -*-

import math

known_numbers = {}

def is_palindrome(n):
    try:
        return known_numbers[n]
    except KeyError:
        s = str(n)
        m = len(s)
        k = m/2
        m -= 1
        for i in range(k):
            if s[i] != s[m-i]:
                known_numbers[n] = False
                return False
                
        known_numbers[n] = True
        return True

def fas_count(start, stop):
    r0 = int(math.floor(math.sqrt(start)))
    r1 = int(math.ceil(math.sqrt(stop+1)))
    
    count = 0
    for i in range(r0, r1):
        v = i*i
        if v >= start and v <= stop:
            if is_palindrome(i) and is_palindrome(v):
                count += 1
            
    return count
    
def process(filename):
    output = open("/Users/gersonkurz/Downloads/fas-input.out", "w")
    for index, line in enumerate(open(filename).readlines()):
        if index:
            start, stop = map(int, line.strip().split())
            print "Case #%d: %d" % (index, fas_count(start, stop), )
            print >>output, "Case #%d: %d" % (index, fas_count(start, stop), )
        
    output.close()
    
if __name__ == "__main__":
    process("/Users/gersonkurz/Downloads/C-small-attempt0.in")
    