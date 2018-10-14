import sys
import re

DEBUG = False

BAD = False

def case_to_re(case):
    cases = case.split("(")
    regex = ""
    for ccase in cases:
        if ccase.find(")") >= 0: # pattern
            ix_p_end = ccase.rfind(")")
            pattern = ccase[:ix_p_end]
            
            regex += "[" + pattern + "]"

            if ix_p_end+1 < len(ccase):
                regex += ccase[ix_p_end+1:]
        else:
            regex += ccase
    return regex

def solve_case(case, words, l):
    # Trivial cases
    if len(case) == 0:
        return 0

    if DEBUG: print case
 
    regex = case_to_re(case)
    if DEBUG: print regex
    p = re.compile(regex)

    mapr = map(lambda x: 1 if p.search(x) else 0, words)

    return reduce(lambda x, y: x+y, mapr)

if __name__ == "__main__":
    input = open(sys.argv[1]).readlines()
    ldn = input[0].split(" ")
    l = int(ldn[0])
    d = int(ldn[1])
    n = int(ldn[2])
    if DEBUG: print "Got l=%d d=%d n=%d" % (l,d,n)
    words = input[1:d+1]
    words = map(lambda x: x.strip(), words)
    cases = input[d+1:d+1+n]
    cases = map(lambda x: x.strip(), cases)
    if BAD:
        cases = ["(abcdefgh)"*15]*500
        words = ["h"*15]*5000
    #print words
    for ix_case in range(len(cases)):
        print "Case #%d: %d" % (ix_case+1, solve_case(cases[ix_case], words, l))
    #print solve_case(cases[0], words, l)
