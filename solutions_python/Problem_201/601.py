from collections import OrderedDict

def solve(inp):
    N, K = map(int, inp.split())
    to_sit = K
    seats = OrderedDict()
    seats[N] = 1
    while True:
        size, count = seats.popitem(False)
        a = size // 2
        b = (size - 1) // 2
        to_sit -= count
        if to_sit <= 0:
            return (a, b)
        if a not in seats:
            seats[a] = 0
        if b not in seats:
            seats[b] = 0
        seats[a] += count
        seats[b] += count

T = int(input())

solutions = [solve(input()) for _ in range(T)]
for i, (y, z) in enumerate(solutions):
    print("Case #{}: {} {}".format(i+1, y, z))
