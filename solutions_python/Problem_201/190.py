#! /usr/bin/python

from collections import defaultdict
import sys
import heapq

def read_case(f):
    return read_space_line(f, int)

def solve(case):
    n, k = case
    y, z = 0, 0
    # Heap of (negative interval length, multiplicity) tuples. Use the negative
    # because this is a minheap.
    intervals = [(-n, 1)]
    while True:
        heapq.heapify(intervals)
        # Mapping from length to multiplicity. This will be flattened into a
        # list and heapified once we exhaust intervals.
        new_intervals = defaultdict(int)
        while intervals:
            length, mult = heapq.heappop(intervals)
            length *= -1
            y, z = insert(length)
            k -= mult
            if k <= 0:
                return "%d %d" % (y, z)
            else:
                new_intervals[-y] += mult
                new_intervals[-z] += mult
        intervals = list(new_intervals.iteritems())
        
def insert(n):
    if n % 2 == 0:
        return n / 2, n / 2 - 1
    else:
        return (n-1)/2, (n-1)/2

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


