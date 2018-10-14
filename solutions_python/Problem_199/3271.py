from collections import deque, Counter

def flip(pancakes, i, k):
    new_pancakes = pancakes[:i] + ["-" if p == "+" else "+" for p in pancakes[i:i+k]] + pancakes[i+k:]
    return new_pancakes


def solve(line):
    pancakes, k = line.split()
    num_pos = pancakes.count("+")
    k = int(k)
    pancakes = list(pancakes)
    flips = 0
    for i in range(len(pancakes)):
        if pancakes[i] == "-":
            flips += 1
            negs = pancakes[i:i+k].count("-")
            num_pos = num_pos - (k-negs) + negs
            pancakes = flip(pancakes, i, k)
        if num_pos == len(pancakes):
            return flips
    return "IMPOSSIBLE"


num = int(input())
for i in range(1, num+1):
    print("Case #{}: {}".format(i, solve(input())))
