#!/usr/bin/env python3

from sys import stdin, stdout, stderr
import math

def minFor2(p1, p2):
    x1, y1, r1 = p1
    x2, y2, r2 = p2
    d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return (d + r1 + r2) * 0.5

def solve_case(case):
    #print(case, file=stderr)
    N, plants = case
    if N == 1:
        return plants[0][2]
    elif N == 2:
        return max(plants[0][2], plants[1][2])
    elif N == 3:
        return min(max(plants[i][2], minFor2(plants[(i + 1) % 3], plants[(i + 2) % 3])) for i in range(3))
        

def read_case():
    N = int(input())
    plants = [tuple(map(int, input().split())) for i in range(N)]
    return N, plants

def print_case(i, ans):
    s = "Case #%d: %.6f" % (i, ans)
    print(s)

def main():
    for i in range(1, int(input()) + 1):
        print_case(i, solve_case(read_case()))

if __name__ == "__main__":
    main()

