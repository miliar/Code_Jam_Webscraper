import sys
import math

sys.setrecursionlimit(10000)
pi = math.pi

t = int(input())

def solve(k, pancakes):
    d = {}
    def solve_rest(k_left, pancakes_left):
        if k_left > len(pancakes_left) or k_left == 0:
            return 0
        pair = (k_left, len(pancakes_left))
        if pair in d:
            return d[pair]
        r, h = pancakes_left[0]
        a = 2 * pi * r * h + solve_rest(k_left - 1, pancakes_left[1:])
        b = solve_rest(k_left, pancakes_left[1:])
        c = max(a, b)
        d[pair] = c
        return c
    m = 0
    for i in range(len(pancakes) - k + 1):
        r, h = pancakes[i]
        area = pi * r * r + 2 * pi * r * h
        area += solve_rest(k - 1, pancakes[i + 1:])
        m = max(m, area)
    return m

for i in range(1, t + 1):
    line = sys.stdin.readline().strip("\n")
    n, k = line.split(" ")
    n, k = int(n), int(k)
    pancakes = []
    for j in range(n):
        line = sys.stdin.readline().strip("\n")
        r, h = line.split(" ")
        r, h = int(r), int(h)
        pancakes.append((r, h))
    pancakes.sort()
    pancakes.reverse()
    solution = solve(k, pancakes)
    print("Case #{}: {}".format(i, solution))
