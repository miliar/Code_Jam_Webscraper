from collections import defaultdict
import math

def top_area(R):
    return math.pi * R * R

def side_area(X):
    R, H = X
    return math.pi * 2 * R * H

def total_area(X):
    R, H = X
    return top_area(R) + side_area(R,H)


T = int(input())


for t in range(T):
    N, K = map(int, input().split())

    max_rad = -1
    max_height = -1
    max_base = 0
    rads = defaultdict(list)
    heights = []
    for n in range(N):
        R, H = map(int, input().split())

        heights.append((R, H))
        rads[R].append(H)

    ans = 0
    arrange = []
    for n in range(N):
        vals = []
        vals.append(heights[n])
        max_r, max_h = heights[n]
        hh = heights[:]
        hh.remove(heights[n])
        for k in range(K-1):
            vals.append(max(hh, key=side_area))
            hh.remove(vals[-1])

            r, h = vals[-1]

            max_r = max(r, max_r)
        temp = 0
        for i in range(len(vals)):
            temp += side_area(vals[i])
        temp += top_area(max_r)
        if temp >= ans:
            arrange = vals
            ans = temp
    print("Case #%d: %f" % (t+1, ans))






