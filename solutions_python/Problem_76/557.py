#!/usr/bin/env python2.6
import sys
import operator
import itertools

def possible_splits(values):
    for n in range(2 ** len(values)):
        a = [value for i, value in enumerate(values) if (n >> i) & 1]
        b = [value for i, value in enumerate(values) if not (n >> i) & 1]
        
        yield a, b

def solve_case(values):
    """Brute force!
    
    I'll find an elegant solution after I have the points to advance."""
    
    best = None
    
    for sean_values, pat_values in possible_splits(values):
        if not (sean_values and pat_values):
            continue # must be nonempty
        
        sean_actual_sum = sum(sean_values)
        
        sean_incorrect_sum = reduce(operator.xor, sean_values)
        pat_incorrect_sum = reduce(operator.xor, pat_values)
        
        if sean_incorrect_sum == pat_incorrect_sum:
            if best is None or best < sean_actual_sum:
                best = sean_actual_sum
    
    if best is not None:
        return best
    else:
        return "NO"

def main(*_ignore):
    cases = [map(int, line.strip().split()) for line in list(sys.stdin)[2::2]]
    
    for n, case in enumerate(cases, 1):
        result = solve_case(case)
        
        print "Case #{0}: {1}".format(n, result)
        

if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))
