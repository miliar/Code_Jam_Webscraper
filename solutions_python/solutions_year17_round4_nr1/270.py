import sys

sys.stdin = open('a.in', 'r')
sys.stdout = open('a.out', 'w')

def ceildiv(a, b):
    return -(-a // b)

def solve():
    N, P = [v for v in map(int, input().split())]
    G = [v for v in map(int, input().split())]

    if P == 2:
        odds = len([v for v in filter(lambda v: v % 2, G)])
        return N - int(odds / 2)

    elif P == 3:
        zero = len([v for v in filter(lambda v: v % 3 == 0, G)])
        ones = len([v for v in filter(lambda v: v % 3 == 1, G)])
        twos = len([v for v in filter(lambda v: v % 3 == 2, G)])

        matching = min(ones, twos)
        c = zero + matching

        ones = ones - matching
        twos = twos - matching

        rest = ceildiv(ones + twos, 3)

        return c + rest






T = int(input())

for i in range(1, T + 1):
    ans = solve()
    print("Case #" + str(i) + ": " + str(ans))