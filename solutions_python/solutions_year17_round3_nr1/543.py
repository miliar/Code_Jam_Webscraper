import math

def side(pancake):
    return pancake[0] * 2 * math.pi * pancake[1]

def top(pancake):
    return pancake[0]**2 * math.pi

t = int(input())
for case in range(1, t + 1):
    n, k = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    pancakes = []
    for i in range(n):
        r, h = [int(s) for s in input().split(" ")]
        pancakes.append((r, h))

    pancakes = sorted(pancakes, key=lambda pancake: pancake[0], reverse=True)

    pancakes = sorted(pancakes, key=lambda pancake: side(pancake) , reverse=True)
    pancakes_short = pancakes[:k]
    pancakes_removed = pancakes[k:]

    min_add_side = side(pancakes_short[-1])
    pancakes_short = sorted(pancakes_short, key=lambda pancake: pancake[0] , reverse=True)
    area = top(pancakes_short[0])
    for pancake in pancakes_short:
        area += side(pancake)

    max_gain = 0
    for pancake in pancakes_removed:
        if pancake[0] > pancakes_short[0][0] and (side(pancake) + top(pancake)) > min_add_side + top(pancakes_short[0]):
            gain = side(pancake) + top(pancake) - (min_add_side + top(pancakes_short[0]))
            if gain > max_gain:
                max_gain = gain

    area += max_gain
    print("Case #{}: {}".format(case, area))
