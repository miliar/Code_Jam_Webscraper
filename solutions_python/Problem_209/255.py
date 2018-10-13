import operator
import math

class Pancake:
    def __init__(self, r, h):
        self.r = r
        self.h = h
        self.vert = 2 * math.pi * r * h
        self.tot = math.pi * r * r + self.vert


T = int(input())
for t in range(1, T+1):
    N, K = [int(_) for _ in input().split(" ")]
    pancakes = []
    for n in range(N):
        R, H = [int(_) for _ in input().split(" ")]
        pancakes.append(Pancake(R, H))
    
    pancakes.sort(key=lambda x: -x.vert)
    ans = 0
    for i,p in enumerate(pancakes):
        thresh = p.r
        res = math.pi * thresh * thresh + p.vert
        count = 1
        for j,g in enumerate(pancakes):
            if count == K:
                break
            if i != j:
                if g.r <= thresh:
                    res += g.vert
                    count += 1
        ans = max(ans, res)
    # print(ans)
    print("Case #{}: {}".format(t, ans))