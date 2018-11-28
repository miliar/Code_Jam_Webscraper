#!/usr/bin/python

import math

in_file_name = raw_input('in file: ')
in_file = open(in_file_name)
out_file = open(in_file_name.split('.')[0]+'.out', 'w')

T = int(in_file.readline())

def is_palindrome(number):
    string_number = str(number)
    return string_number == string_number[::-1]

for test_case_number in range(T):
    
    A,B = [int(_) for _ in in_file.readline().split(' ')]
    fair_and_square = 0
    A_square_root = int(math.ceil(A**.5))
    B_square_root = int(math.floor(B**.5))

    for number in range(A_square_root, B_square_root+1):
        if is_palindrome(number) and is_palindrome(number**2):
            fair_and_square +=1
    out_file.write('Case #%i: %i' % (test_case_number+1, fair_and_square))
    if test_case_number < T-1: 
        out_file.write('\n')

out_file.close()
         
 
