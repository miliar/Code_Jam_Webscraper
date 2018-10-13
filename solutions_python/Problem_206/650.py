import sys
import numpy as np

input_file = "A-large.in"
output_file = "A-large.out"


def solve(tt):
    d, n = [int(j) for j in input().split(" ")]
    p = [0]*n
    v = [0]*n
    t = [0]*n
    for i in range(n):
        p[i], v[i] = [int(j) for j in input().split(" ")]
        t[i] = (d-p[i])/v[i]
    max_t = np.max(t)
    return d/max_t


def main():
    t = int(input())
    for tt in range(1, t + 1):
        answer = solve(tt)
        print("Case #{}: {}".format(tt, answer))

if __name__ == "__main__":
    sys.stdin = open(input_file)
    sys.stdout = open(output_file, 'w+')
    main()