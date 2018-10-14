# Lawnmower
# https://code.google.com/codejam/contest/2270488/dashboard#s=p1

# PYTHON 3

import sys

sys.stdin = open('b.in', 'r')
sys.stdout = open('b.out', 'w')


def all_same(items):
    return all(x == items[0] for x in items)


t = int(input())

for T in range(1, t + 1):
    n, m = [int(x) for x in input().split()]
    if n == 1 or m == 1:
        for x in range(n):
            input()
        print("Case #%d: YES" % T)
        continue
    lawn = []
    lawn_vertical = [[] for x in range(m)]
    for i in range(n):
        line = [int(x) for x in input().split()]
        lawn.append(line)
        for j in range(m):
            lawn_vertical[j].append(line[j])

    break_loop = False
    for i in range(n):
        line = lawn[i]
        max_height = max(line)
        min_height = min(line)
        if not max_height == min_height:
            for j in range(m):
                # check horizontal
                if not line[j] == max_height:
                    # check vertical
                    if all_same(lawn_vertical[j]):
                        continue
                    else:
                        print("Case #%d: NO" % T)
                        break_loop = True
                        break
        if break_loop:
            break
    if not break_loop:
        print("Case #%d: YES" % T)
