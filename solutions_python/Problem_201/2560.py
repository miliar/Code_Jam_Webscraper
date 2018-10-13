

import sys
import numpy as np

input_file = "C-small-1-attempt0.in"
output_file = "C-small-1-attempt0.out"

def solve(n, k):
    diffs = np.array([n])
    for i in range(k):
        m = np.max(diffs)
        arg_m = np.argmax(diffs)
        if i == k-1:
            if m % 2 == 0:
                smin = m/2-1
                smax = m/2
            else:
                smin = smax = (m-1)/2
            return smin, smax
        else:
            if m % 2 == 0:
                diffs[arg_m] = m/2
                diffs = np.insert(diffs, arg_m, m/2-1)
            else:
                diffs[arg_m] = (m-1)/2
                diffs = np.insert(diffs, arg_m, (m-1)/2)
    return -1

def main():
    t = int(input())
    for i in range(1, t + 1):
        n, k = [int(j) for j in input().split(" ")]
        smin, smax = solve(n, k)
        print("Case #{}: {} {}".format(i, int(smax), int(smin)))

if __name__ == "__main__":
    sys.stdin = open(input_file)
    sys.stdout = open(output_file, 'w+')
    main()