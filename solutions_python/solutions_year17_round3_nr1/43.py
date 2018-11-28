import operator
import math
import pdb

t = int(input())

def getScore(pancakes):
    total = 0
    for cake in pancakes:
        total += cake[1]

    biggest = max(pancakes, key = operator.itemgetter(0))

    return total + biggest[0]

for i in range(t):
    s = input().split(" ")
    n = int(s[0])
    k = int(s[1])
    pancakes = []
    for _ in range(n):
        s = input().split(" ")
        radius = int(s[0])
        height = int(s[1])
        top = math.pi*radius*radius
        edge = 2*math.pi*radius*height

        pancakes.append((top, edge))

    pancakes.sort(key=operator.itemgetter(1), reverse=True)

    others = pancakes[k-1:]

    pancakes = pancakes[:k-1]

    highest = 0

    for cake in others:
        highest = max(highest, getScore(pancakes+[cake]))

    print("Case #{}: {}".format(i+1, highest))
