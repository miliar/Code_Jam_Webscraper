import math

def get_area(last_pencake, left_pancakes):
    return math.pi * (last_pencake[0] ** 2 + 2 * last_pencake[0] * last_pencake[1] + sum([pancake[0] * pancake[1] * 2 for pancake in left_pancakes]))

def solve(N, K, pancakes):
    max_area = 0
    pancakes.sort(key=lambda pancake: pancake[0], reverse=True)
    for i in range(N):
        last_pencake = pancakes[i]
        left_pancakes = sorted(pancakes[i+1:], key=lambda pancake: pancake[0] * pancake[1], reverse=True)[:K-1]

        max_area = max(max_area, get_area(last_pencake, left_pancakes))

    return max_area

T = int(input())
for t in range(T):
    N, K = [int(x) for x in input().split()]
    pancakes = []
    for n in range(N):
        pancakes.append([int(x) for x in input().split()])

    area = solve(N, K, pancakes)

    print("Case #%d: %.9f" % (t+1, area))