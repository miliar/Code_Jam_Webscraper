#! /usr/bin/python

import sys

def read_case(f):
    return read_space_line(f, int)[0]

def solve(case):
    acc = 0
    lowest_no = 9
    curr_pow = 0
    while case > 0:
        next_digit = case % 10
        if next_digit <= lowest_no:
            lowest_no = next_digit
        else:
            # We found an inversion, reset at 9*
            # We know next_digit > 0, so the below is valid
            next_digit -= 1
            lowest_no = next_digit
            acc = (10 ** curr_pow) - 1
        acc += next_digit * (10 ** curr_pow)
        curr_pow += 1
        case //= 10
    return acc

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


