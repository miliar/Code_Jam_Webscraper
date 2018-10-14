import sys

sys.stdin = open(sys.argv[1], 'r')

def f():
    pancakes, n = input().split()
    n = int(n)
    pancakes = [x == '+' for x in pancakes]
    flips = 0
    for i in range(len(pancakes) - n + 1):
        if not pancakes[i]:
            for j in range(i, i + n):
                pancakes[j] = not pancakes[j]
            flips += 1
    if all(pancakes):
        return flips
    else:
        return "IMPOSSIBLE"

for t in range(1, int(input()) + 1):
    print("Case #%d:" % t, f())