import sys
import re

DEBUG = False

BAD = False

def last(l):
    return(l[len(l)-1])

def get_opposed(opposed, x):
    if opposed[0] == x:
        return opposed[1]
    else:
        return opposed[0]

def try_combine(x, y, combine):
    for comb in combine:
        if (x == comb[0] and y == comb[1]) or (x == comb[1] and y == comb[0]): 
            return comb[2]
    return None

def invoke(magic, combine, oppose):
    out = []
    done = False
    for x in magic:
        if len(out) == 0:
            out.append(x)
        else:
            done = False
            # Check for combining elements
            last_elem = last(out)
            combined = try_combine(x, last_elem, combine)
            if combined:
                done = True
                out.pop()
                out.append(combined)
            else:
            # Check for opposing elements
                for opp in oppose:
                    if x in opp:
                        opposed = get_opposed(opp, x)
                        if opposed in out:
                            out = []
                            done = True
            if not done:
                out.append(x)
        if DEBUG: print out
            
    return out

def solve_case(case):
    # Trivial cases
    if len(case) == 0:
        return 0

    ccase = case.split(" ")
    ccase.reverse()

    c = int(ccase.pop())
    combine = []
    for x in range(c):
        combine.append(ccase.pop())

    d = int(ccase.pop())
    oppose = []
    for x in range(d):
        oppose.append(ccase.pop())

    N = int(ccase.pop())
    magic = ccase.pop()

    return invoke(magic, combine, oppose)

def print_out(out):
    sout = "["
    for x in range(len(out)):
        sout += str(out[x])
        if x < (len(out) - 1):
            sout += ", "
    return sout + "]"

if __name__ == "__main__":
    input = open(sys.argv[1]).readlines()
    ldn = input[0].split(" ")
    t = int(input[0])
    if DEBUG: print "Got t=%d" % (t)
    cases = input[1:t+1]
    cases = map(lambda x: x.strip(), cases)
    if BAD:
        cases = ["(abcdefgh)"*15]*500
    #print words
    for ix_case in range(len(cases)):
        print "Case #%d: %s" % (ix_case+1, print_out(solve_case(cases[ix_case])))
    #print solve_case(cases[0], words, l)
