#import sys

n = int(input())


def solve(a, Ta, b, Tb):
    intersect = set(Ta[a-1]) & set(Tb[b-1])

    if len(intersect) == 1:
        return intersect.pop()
    elif len(intersect) > 1:
        return "Bad magician!"

    return "Volunteer cheated!"

for i in range(n):
    a = int(input())
    Ta = [list(map(int, input().split())) for _ in range(4)]

    b = int(input())
    Tb = [list(map(int, input().split())) for _ in range(4)]

    print("Case #{}: {}".format(i+1, solve(a, Ta, b, Tb)))
