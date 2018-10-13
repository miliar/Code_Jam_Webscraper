#!/usr/bin/env python

import sys
from operator import xor

opposed = {}
combined = {}
 
# mv ~/Downloads/C-small-attempt1.in .
# time ./B-small-0.py < B-small-attempt0.in > B-small-attempt0.out

def start_solve(in_set):
    global opposed, combined
    opposed = {}
    combined = {}

    in_data = in_set.split()

    for i in range(int(in_data.pop(0))):
        j = in_data.pop(0)
        combined[(j[0], j[1])] = j[2]
        combined[(j[1], j[0])] = j[2]

    for i in range(int(in_data.pop(0))):
        j = in_data.pop(0)
        opposed[j[0]] = opposed.get(j[0], "") + j[1]
        opposed[j[1]] = opposed.get(j[1], "") + j[0]

    run_len = int(in_data.pop(0))
    run_str = in_data.pop(0)

    return do_solve(run_str)

def do_solve(in_str):
    global opposed, combined

    in_str = list(in_str)
    out_str = []

    while in_str:
        # print out_str, in_str
        new_char = in_str.pop(0)

        if len(out_str) == 0:
            out_str.append(new_char)
            continue

        if combined.get((new_char, out_str[-1])):
            in_str = [combined[(new_char, out_str[-1])]] + in_str
            out_str.pop()
            continue

        if new_char in opposed:
            if any(char1 in out_str for char1 in opposed[new_char]):
                out_str = []
                continue

        out_str.append(new_char)
 
    return out_str

def proc_input():
    num_cases = int(raw_input())

    global res_sum

    for i in range(num_cases):
        arr = raw_input()
        out = start_solve(arr)

        out = ", ".join(out)
        print "Case #%i: [%s]" % (i+1, out)       

if __name__ == "__main__":
    proc_input()
