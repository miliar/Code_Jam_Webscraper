from __future__ import print_function
import sys

def flip(t):
    pancakes, k = t.split(" ")
    pancakes = map(lambda p: 1 if p == "+" else 0, list(pancakes))
    k = int(k)
    flips = 0
    for i in range(len(pancakes) - k + 1):
        if pancakes[i] == 0:
            for j in range(k):
                pancakes[i + j] ^= 1
            flips += 1
    if 0 in pancakes:
        return "IMPOSSIBLE"
    else:
        return str(flips)

data = sys.stdin.readlines()

n = int(data[0])

for i in range(1, 1 + n):
    line = data[i].strip()
    print("Case #{}: {}".format(i, flip(line)))
