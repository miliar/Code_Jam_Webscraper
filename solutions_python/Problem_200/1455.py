#!/usr/bin/env python
import sys
from math import log10, floor
lines = [l.strip() for l in sys.stdin.readlines()]
T = int(lines[0])
assert(T == len(lines)-1)

def make_more_tidy_number(num):
    result = False
    mul = 1
    cntr = int(num)
    delta = 1
    while True:
        shifted = cntr / mul
        if shifted < 1: 
            break
        digit = shifted % 10
        if digit > 0:
            delta += digit*mul            
        next_digit = (shifted/10) % 10
        if digit < next_digit:
            cntr -= delta
            delta = 0
            result = True
        mul *= 10
    return result, cntr

def is_tidy(num):
    cntr = int(num)
    prev_digit = cntr % 10
    cntr /= 10
    while cntr > 0:
        digit = cntr % 10
        if digit > prev_digit:
            return False
        cntr /= 10
        prev_digit = digit      
    return True  

def tidy_number(num):
    cntr = num
    while not is_tidy(cntr):
        cntr -= 1
    return cntr

def tidy_number_fast(num):
    cont = True
    while cont:
        cont, num = make_more_tidy_number(num)
    assert(is_tidy(num)) 
    return num

for i in range(1, T+1):
    num = int(lines[i].strip())
    sys.stdout.write("Case #{}: {}\n".format(i, tidy_number_fast(num)))
