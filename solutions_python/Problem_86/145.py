#!/usr/bin/env python

# mv ~/Downloads/C-small-attempt0.in .
# time ./run-task.py < C-small-attempt0.in > C-small-attempt0.out

def harm(f1, f2):
    return f1 % f2 == 0 or f2 % f1 == 0

def start_solve(n, low, high, data):
    if low == 1:
        return 1

    for f in range(low, high+1):
        if all([harm(f,pf) for pf in data]):
            return f

    return "NO"

def proc_input():
    num_cases = int(raw_input())

    for i in range(num_cases):
        # need to read all parameters
        n, low, high = [int(x) for x in raw_input().split()]
        arr = [int(x) for x in raw_input().split()]

        out = start_solve(n, low, high, arr)

        print "Case #%i: %s" % (i+1, out)       

if __name__ == "__main__":
    proc_input()
