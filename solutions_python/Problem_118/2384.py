#!/usr/bin/env python

import math

input_file = 'fairsquare-small.dat'

def is_palindrome(n):
    n_str = str(n)
    n_rev = int(n_str[::-1])
    
    return (n == n_rev)
    

with open (input_file, 'r') as data_file:
    N_tests = int(data_file.readline())
    
    for i in range(0,N_tests):
        (A, B) = map(int, data_file.readline().split())
        num_FS = 0
        
        root_A = int(math.ceil(math.sqrt(A)))
        root_B = int(math.floor(math.sqrt(B)))

        for n in range(root_A, root_B+1):
            if (is_palindrome(n)):
                if (is_palindrome(n*n)):
                    num_FS += 1

        case_str = "Case #{0:d}: {1:d}".format(i+1, num_FS)
        print case_str