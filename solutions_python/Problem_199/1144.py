import math
from sortedcontainers import SortedList
from multiprocessing import Pool

debug = False

def dbg_print(x):
    if debug:
        print(x)

def solve(input):
    index, s, k = input
    l = len(s)
    flips = 0
    dbg_print("== case #{} len = {} str =".format(index,l))
    dbg_print(''.join(s))
    for i in range(0, l-(k-1)):
        dbg_print("[{}]:{}".format(i,s[i]))
        if s[i] == '-':
            s[i]   = '+'
            for j in range(1,k):
                s[i+j] = '+' if s[i+j] == '-' else '-'
            flips = flips + 1
            dbg_print(''.join(s))

    if '-' in s:
        solution = "IMPOSSIBLE"
    else:
        solution = flips

    dbg_print("solution: {}".format(solution))

    return (index, solution)


def main():
    # input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(input())  # read a line with a single integer
    inputs = []
    for i in range(1, t + 1):
        s, k = [s for s in input().split(" ")]  # read a string and an int
        s = list(s)
        k = int(k)
        inputs.append( (i,s,k) )

    dbg_print("--- Inputs ---")
    dbg_print(inputs)
    p = Pool(8)
    results = p.map(solve, inputs)
    dbg_print("--- Results ---")
    dbg_print(results)
    results.sort()

    for i, x in results:
        print("Case #{}: {}".format(i, x))

if __name__ == "__main__":
    main()
