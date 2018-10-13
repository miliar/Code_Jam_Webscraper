from __future__ import division
from __future__ import print_function


def solve(x, c, f):
    cookies_per_sec = 2;
    elapsed_time = 0;

    # short circuit
    if x <= c:
        elapsed_time = x / cookies_per_sec;
        return elapsed_time


    while True:
        if x / (cookies_per_sec + f) < (x - c) / cookies_per_sec:
            elapsed_time += c / cookies_per_sec
            cookies_per_sec += f
        else:
            elapsed_time += x / cookies_per_sec;
            return elapsed_time


def main():
    testcases = int(input())
    for t in range(1, testcases + 1):
        (c, f, x) = [float(d) for d in input().split()]
        s = solve(x, c, f)
        print("Case #", t, ': ', s, sep="")

if __name__ == '__main__':
    main()
