#! /usr/bin/python

import sys
from collections import defaultdict

def read_case(f):
    n, p = read_space_line(f, int)
    nums = read_space_line(f, int)
    return n, p, nums

def make_pair(chocs, p):
    if chocs[0] > 0:
        chocs[0] -= 1
        return True
    if p == 2:
        # Just need to handle the 1 case.
        if chocs[1] >= 2:
            chocs[1] -= 2
            return True
    elif p == 3:
        if chocs[1] > 0 and chocs[2] > 0:
            chocs[1] -= 1
            chocs[2] -= 1
            return True
        elif chocs[1] >= 3:
            chocs[1] -= 3
            return True
        elif chocs[2] >= 3:
            chocs[2] -= 3
            return True
    elif p == 4:
        if chocs[2] >= 2:
            chocs[2] -= 2
            return True
        elif chocs[1] > 0 and chocs[3] > 0:
            chocs[1] -= 1
            chocs[3] -= 1
            return True
        elif chocs[1] >= 2 and chocs[2] > 0:
            chocs[1] -= 2
            chocs[2] -= 1
            return True
        elif chocs[3] >= 2 and chocs[2] > 0:
            chocs[3] -= 2
            chocs[2] -= 1
            return True
        elif chocs[1] >= 4:
            chocs[1] -= 4
            return True
        elif chocs[3] >= 4:
            chocs[3] -= 4
            return True

    return False

def solve(case):
    n, p, nums = case
    num_to_count = defaultdict(int)
    for num in nums:
        num_to_count[num % p] += 1
    total = 1  # For the first
    while make_pair(num_to_count, p):
        total += 1
    # Need to check if the last good set of groups ended right at the tail.
    if sum(num_to_count.values()) == 0:
        total -= 1
    return total

# Edit over here --------

def read_space_line(f, constr):
    # Reads a space-delimited line with constructor.
    line = f.readline().strip().split(' ')
    return tuple(int(x) for x in line)

def read_line(f, constr):
    return constr(f.readline().strip())

def input_iterator(in_fn):
    with open(in_fn) as f:
        num_cases = read_line(f, int)
        for i in range(num_cases):
            yield read_case(f)

def write_output(f, case_n, sol_str):
    f.write("Case #%d: %s\n" % (case_n, sol_str))

def main():
    in_fn = sys.argv[1] 
    out_fn = sys.argv[2]
    
    with open(out_fn, 'w') as out_f:
        for i, case in enumerate(input_iterator(in_fn)):
            sol_str = solve(case)
            write_output(out_f, i+1, sol_str)

if __name__ == "__main__":
    main()


