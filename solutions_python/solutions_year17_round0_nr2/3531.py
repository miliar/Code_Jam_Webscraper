'''
Created on Apr 8, 2016

@author: Thomas
'''
import sys
from math import log10, floor
from random import randint

def is_tidy(num):
    s = str(num)
    
    is_tidy = True
    digit_prev = 0
    for digit in s:
        if int(digit) < digit_prev:
            is_tidy = False
        digit_prev = int(digit)
    
    return is_tidy

def get_digits(N):
    s = str(N)
    return [int(digit_s) for digit_s in s]

def get_digits_diff(N):
    digits = get_digits(N)
        
    digits_shifted = list(digits)
    
    digits.pop()
    digits_shifted.pop(0)
    
    diff = []
    for i in range(len(digits)):
        diff.append(digits_shifted[i] - digits[i])
        
    return diff

def find_last_tidy(N):
    Ns = str(N)
    
    diff = get_digits_diff(N)
    
    digits_decreased = [(idx) for idx,x in enumerate(diff) if x < 0]

    if not digits_decreased:
        return N
    
    lowest_digit_idx = min(digits_decreased)
    ldi = lowest_digit_idx
        
    digits = get_digits(N)

    digits[ldi] = digits[ldi] - 1
    for idx,digit in enumerate(digits):
        if idx >= (ldi + 1):
            digits[idx] = 9
    
    num = 0
    for idx,digit in enumerate(digits):
        powy = len(digits) - idx - 1
        num += (10**powy * digit)        
    if is_tidy(num):
        return num
    else:
        return find_last_tidy(num)


if __name__ == '__main__':
    out = {}
    with open("B-large.in", 'rb') as f:
        lines = f.readlines()[1:]
        for idx,line in enumerate(lines):
            line = line.rstrip()
            N = int(line)

            print line + str("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
            N_tidy = find_last_tidy(N)
            print N_tidy
            out[idx+1] = N_tidy


    with open("output.out", 'w') as f:
        f.write("")
        for key, val in out.iteritems():
            line = "Case #" + str(key) + ": " + str(val) + "\n"
            f.write(line)