#! /usr/bin/env python
import sys

def decimal_to_base(decimal, target_radix):
    digits = []
    
    place = 1
    while decimal > 0:
        this_place = decimal % (target_radix**place)

        target_value = this_place / (target_radix**(place - 1))
        
        if target_value > 0:
            digits.append(target_value)
        
        place += 1
        decimal -= this_place
    
    return digits

def happy(digits, radix):
    visited = set()

    result = 0
    while True: 
        for d in digits:
            result += d*d
            
        if result == 1:
            return True
        elif result in visited:
            return False
        else:
            visited.add(result)
            digits = decimal_to_base(result, radix)
            result = 0
        
test_cases = int(sys.stdin.readline().strip())
for test_case in range(test_cases):
    
    integers = map(int, sys.stdin.readline().strip().split(" "))
    
    minimum = 1
    happy_in_all = False
    while not happy_in_all:
        minimum += 1
        happy_in_all = True
        for i in integers:
            if i == 2: # all numbers in base-2 are happy
                continue
        
            happy_in_all = happy_in_all and happy(decimal_to_base(minimum, i), i)

    print "Case #%d: %d" % (test_case + 1, minimum)