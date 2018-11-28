#!/usr/bin/env python3

import logging
import math
import sys

logger = logging.getLogger()
#logging.basicConfig(level=logging.DEBUG, 
#        stream=sys.stderr, format='CJ17.QR.B %(levelname)s %(message)s')

def problem_cases():
    num_cases_total = -1
    num_cases_passed = 0
    
    for count, line in enumerate(sys.stdin):
        line = line.rstrip()
        
        if count == 0:
            num_cases_total = int(line)
            logger.debug('{} cases in total.'.format(num_cases_total))
            continue
        
        logging.debug('Case #{} {}'.format(count, line))
        num_cases_passed += 1
        yield (count, line)
    
    assert num_cases_passed == num_cases_total
    


def solve(n):
    logging.debug('Input: {}'.format(n))
    while True:
        ind = -1
        for i in range(len(n) - 1):
            if int(n[i]) > int(n[i+1]):
                ind = i
                break
        
        if ind < 0:
            solution = int(n)
            logging.debug('Found tidy number {}\n'.format(solution))
            return solution
        else:
            logging.debug('not tidy @ position {}'.format(ind))
            l = n[:ind] + str(int(n[ind]) - 1) + '9' * (len(n) - ind - 1)
            n = str(l)
            
    

        
    
if __name__ == '__main__':
    print('GOOGLE CODEJAM 2017 - Qualification Round - Problem B', file=sys.stderr)
    for case_id, case in problem_cases():
        solution = solve(case)
        print('Case #{}: {}'.format(case_id, solution))
        

