#! /usr/bin/python

import sys
import math

def find_fair_squares(lower, upper):
    fair_square_count = 0
    for num in range(lower, upper+1):
        num_sqrt = math.sqrt(num)
        num_sqrt_floor = math.floor(num_sqrt)
        if num_sqrt != num_sqrt_floor:
            continue
        if not is_palindrome(num) or not is_palindrome(int(num_sqrt)):
            continue
        fair_square_count += 1 
    return fair_square_count

def is_palindrome(num):
    int_str = str(num)
    left = 0
    right = len(int_str) - 1
    
    while left < right:
        if int_str[left] != int_str[right]:
            return False
        left += 1
        right -= 1

    return True
        
def main():
    input_file = sys.argv[1]
    with open(input_file, 'r') as f:
        num_tests =  int(f.readline())
    
        for test in range(num_tests):
            num_range = f.readline().split()
            lower = int(num_range[0])
            upper = int(num_range[1])
            fair_square_count = find_fair_squares(lower, upper)
            print 'Case #%i: %i' % (test+1, fair_square_count)
        
if __name__ == '__main__':
    main()
