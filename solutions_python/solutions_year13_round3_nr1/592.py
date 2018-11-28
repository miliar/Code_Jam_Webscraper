#!/usr/bin/env python
NUM_OF_ELEMENTS_PER_PROBLEM = 1

VOWELS = ['a', 'e', 'i', 'o', 'u']

def find_nths(begin, nth, word):
    end = begin + nth
    result = set()
    while end <= len(word):
        consecutive = int(0)
        for c in word[begin:end]:
            if c not in VOWELS:
                consecutive += 1
                if consecutive >= nth:
                    result.add((word[begin:end],begin))
            else:
                consecutive = 0

        end += 1
    return result

def solve(probleminput):
    """
    in: expects a list of inputs for the current testcase. see NUM_OF_ELEMENTS_PER_PROBLEM for the list size
    out: should return the solution for this testcase
    """
    (word,nth) = probleminput[0].split(' ')
    nth = int(nth)
    
    start = int(0)
    to = len(word) - nth
    nths_found = set()
    
    while start <= to:
        #print "checking: " + word[start:]
        map(lambda x: nths_found.add(x), find_nths(start, nth, word))
        start += 1
        
    #print nths_found
    return len(nths_found)

###### program skeleton #######
import sys
if __name__ == "__main__":
    problem = [l.replace('\n','') for l in sys.stdin.readlines()]
    for testcase in xrange(1, int(problem[0]) + 1):
        begin = 1 + (testcase -1) * NUM_OF_ELEMENTS_PER_PROBLEM
        #if testcase == 2:
        result = solve(problem[begin:begin+NUM_OF_ELEMENTS_PER_PROBLEM])
        print "Case #%i: %s" % (testcase, result)
