# faster version with SortedList and 8 processes
# 35 seconds on C-small-2-attempt0.in

import math
from sortedcontainers import SortedList
from multiprocessing import Pool

debug = False

def dbg_print(x):
    if debug:
        print(x)

def split_stalls(intervals):
    big = intervals.pop()
    split = (big-1)/2
    low = math.floor( split )
    hi  = math.ceil ( split )

    if hi != 0:
        intervals.add(hi)
        if low != 0:
            intervals.add(low)
 
    return intervals

def last_split(intervals):
    big = intervals.pop()
    low = math.floor( (big - 1) / 2 )
    hi  = math.ceil ( (big - 1) / 2 )
    return (hi, low)

def solve(input):
    global cases
    i, n, k = input

    intervals = SortedList()
    intervals.add(n)
    dbg_print(n)
    for j in range(0, k-1):
        intervals = split_stalls(intervals)
    dbg_print(intervals)
    (x,y) = last_split(intervals)

    return (i, x, y)

def main():
    global cases
    # input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(input())  # read a line with a single integer
    inputs = []
    for i in range(1, t + 1):
        n, k = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
        inputs.append( (i,n,k) )

    dbg_print("--- Inputs ---")
    dbg_print(inputs)
    p = Pool(8)
    results = p.map(solve, inputs)
    dbg_print("--- Results ---")
    dbg_print(results)
    results.sort()

    for i, x, y in results:
        print("Case #{}: {} {}".format(i, x, y))

if __name__ == "__main__":
    main()
