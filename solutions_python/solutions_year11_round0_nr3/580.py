from functools import reduce

def patsum(candies):
    return reduce(lambda x, y: x^y, candies)

def solve(candies):
    if patsum(candies) != 0:
        return "NO"
    candies.remove(min(candies))
    return sum(candies)

t = int(input())
for case in range(t):
    # discard N; don't need it
    input()
    candies = list(map(int, input().split(' ')))
    print("Case #%d:" % (case+1), solve(candies))
