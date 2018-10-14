# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 23:55:48 2013

@author: soj
"""

import math

def num_palindromes(start, end):
    count = 0
    for i in xrange(start, end + 1):
        st_val = str(i)
        if st_val == st_val[::-1]:
            sqrt = math.sqrt(i)
            if(sqrt%1 == 0):
                string_val = str(int(sqrt))
                if string_val == string_val[::-1]:
                    count += 1
    return count


number_of_test_cases = None
ins = open( "input", "r" )
case = 0
start = None
end = None
for l in ins:
    line = l.strip()
    if(number_of_test_cases is None):
        number_of_test_cases = int(line)
    else:
        array = line.split(' ')
        start = int(array[0])
        end = int(array[1])
        case += 1
        print "Case #" + str(case) + ": " + str(num_palindromes(start, end))

    if(case == number_of_test_cases):
        break;

