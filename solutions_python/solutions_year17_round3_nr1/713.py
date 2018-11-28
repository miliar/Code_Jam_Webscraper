from bisect import bisect
from itertools import combinations
from math import pi

def pancake_longest_decreasing(radii, heights, K):
    end = []
    m = []
    prev = []
    for i, n in enumerate(radii):
        if not end:
            end.append(-n)
            m.append(0)
            prev.append(-1)
        elif n <= -end[-1]:
            end.append(-n)
            m.append(i)
            prev.append(m[-1])
        else:
            location = bisect(end, -n)
            end[location] = -n
            if location == 0:
                prev.append(-1)
            else:
                prev.append(m[location-1])
            m[location] = i

    best_score = 0
    for c in combinations(range(len(m)), K):
        comb_loc = len(c)-1
        x = m[c[comb_loc]]
        score = 0
        while True:
            score += 2*pi*heights[x]*radii[x]
            if comb_loc == 0:
                score += (pi*(radii[x]**2))
                break
            comb_loc -= 1
            x = m[c[comb_loc]]
        best_score = max(score, best_score)
    return best_score

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split(' '))
    pancakes = []
    for pancake in range(N):
        R, H = map(int, input().split(' '))
        pancakes.append((R, H))
    pancakes.sort(key=lambda x:x[0], reverse=True)
    radii = [x[0] for x in pancakes]
    heights = [x[1] for x in pancakes]
    score = pancake_longest_decreasing(radii, heights, K)
    print('Case #', t, ': ', score, sep='')




