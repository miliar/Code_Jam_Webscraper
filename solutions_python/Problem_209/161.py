import sys
import math
PI = math.pi
def solve(K, pancakes):
    heights = []
    for idx, pancake in enumerate(pancakes):
        r, h = pancake
        heights.append((2 * PI * r * h, idx))
    heights = sorted(heights, reverse=True)

    max_sum = 0
    for idx, pancake in enumerate(pancakes):
        r, h = pancake
        area = PI * (r*r)
        cyl = 2*PI*r*h
        amt = area + cyl
        ind = 0 
        total = 0
        while total+1 < K:
            cyl_area, idval = heights[ind]
            if idx != idval:
                amt += cyl_area
                total += 1
            ind += 1
        if amt > max_sum:
            max_sum = amt
    return max_sum

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for case in range(T):
        pancakes = []
        N, K = map(int, sys.stdin.readline().split())
        for cake in range(N):
            r, h = map(int, sys.stdin.readline().split())
            pancakes.append((r, h))
        print "Case #{}: {:.9f}".format(case + 1, solve(K, pancakes))

