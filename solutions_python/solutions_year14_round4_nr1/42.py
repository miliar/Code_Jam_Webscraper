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
    filenum, size = (int(x) for x in problem_input.readline().split())
    sizes = sorted(int(x) for x in problem_input.readline().split())
    start = 0
    end = len(sizes) - 1
    count = 0
    while start < end:
        if sizes[end] + sizes[start] <= size:
            start +=1
        end -= 1
        count += 1
    if start == end:
        count += 1
    
    return count
    
   
            
if __name__ == "__main__":
    main()
