#!/usr/bin/env python

import sys
from operator import xor

def start_solve(tmp_len, in_set):
    global set_buf, res_sum

    res_sum = 0
    set_buf = set()

    in_set = [ int(x) for x in in_set.split() ]

    tmp_xor1 = 0
    tmp_xor2 = reduce(xor, in_set)
    tmp_sum = sum(in_set)

    do_solve(in_set, tmp_len, tmp_xor1, tmp_xor2, tmp_sum)

res_sum = 0

set_buf = set()

def do_solve(in_set, tmp_len, tmp_xor1, tmp_xor2, tmp_sum):
    global res_sum, set_buf

    if tmp_len == 0:
        return

    if tuple(in_set) in set_buf:
        return
    else:
        set_buf.add(tuple(in_set))

#    print tmp_len, in_set

 #   sys.stdout.flush()

    for i in range(tmp_len):
        if in_set[i] ^ tmp_xor1 == in_set[i] ^ tmp_xor2:
            # solution found
            res_sum = max(res_sum, tmp_sum - in_set[i])

    for i in range(tmp_len):
        # if the potential total is larger than already found
        if tmp_sum - in_set[i] > res_sum:
            out_set = in_set[:]
            out_set.pop(i)
            do_solve(out_set, tmp_len-1, in_set[i] ^ tmp_xor1, in_set[i] ^ tmp_xor2, tmp_sum - in_set[i])

def test_solve1():
    arr = "1 2 3 4 5"
    start_solve(len(arr.split()), arr)        

def test_solve2():
    arr = "3 5 6"
    start_solve(len(arr.split()), arr)        

def proc_input():
    num_cases = int(raw_input())

    global res_sum

    for i in range(num_cases):
        res_sum = 0

        len_arr = int(raw_input())
        arr = raw_input()
        
        start_solve(len_arr, arr)

        print "Case #%i: %s" % (i+1, res_sum or "NO")       

if __name__ == "__main__":
    proc_input()
