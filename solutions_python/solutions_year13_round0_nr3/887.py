import math
from pprint import pprint
import pickle
import os
import sys

def generate_squares(start, end):
    end_num = int(math.floor(end**0.5))
    return [i**2 for i in range(start, end_num) if check_palindrome(str(i))]

def check_palindrome(s):
    s = str(s)

    for i in range(0, len(s)/2):
        #print 'check {0} == {1}'.format(s[i], s[len(s)-1-i])
        if s[i] != s[len(s)-1-i]:
            return False
    return True

def choose_squares(start, end, squares):
    return [ x for x in squares if x >= start and x <= end ]


if __name__ == '__main__':
    squares = generate_squares(1, 10**14)

    #print 'done squares'

    case_num = int(sys.stdin.readline().strip())
    cases = [line.strip().split(" ") for line in sys.stdin.readlines() ]

    #pprint(cases)

    for n, raw_input_case in enumerate(cases):
        input_case = int(raw_input_case[0]), int(raw_input_case[1])

        fair_palindrome_candidates = choose_squares( input_case[0], input_case[1], squares)
        #pprint(fair_palindrome_candidates)
        result_l = map(check_palindrome, fair_palindrome_candidates)
        #pprint(result_l)

        result_count = result_l.count(True)

        #pprint(result_count)

        title = "Case #{0}: {1}\n".format(n+1, result_count)
        sys.stdout.write(title)

        

    


    
        
    

