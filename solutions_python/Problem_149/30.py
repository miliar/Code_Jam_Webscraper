'''
Created on Apr 12, 2014

@author: ignacio
'''

import sys
import logging
import os

if "--debug" in sys.argv:
    logging.basicConfig(level=logging.DEBUG)


def main():
    problem_input = sys.stdin
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        if os.path.isfile(input_file):
            problem_input = open(input_file)
        
    cases = int(problem_input.readline())
    logging.debug(cases)
    for case in xrange(cases):
        resp = run_case(problem_input)
        print "Case #%s: %s" % (case + 1, resp,)
    
            
def run_case(problem_input):
    size = (int(x) for x in problem_input.readline().split())
    values = [int(x) for x in problem_input.readline().split()]
    maxi = max(values)
    maxi_pos = values.index(maxi)
    start = maxi_pos
    cost = 0
    end = start + 1
    while start > 0 :
        value = values[start - 1]
        left_cost = len([x for x in values[:start] if x > value])
        right_cost = len([x for x in values[start:] if x > value])
        cost += min(left_cost, right_cost)
        start -= 1
    while end < len(values):
        value = values[end]
        left_cost = len([x for x in values[:end] if x > value])
        right_cost = len([x for x in values[end:] if x > value])
        cost += min(left_cost, right_cost)
        end += 1
        
    return cost
   
            
if __name__ == "__main__":
    main()
