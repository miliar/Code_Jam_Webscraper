# 0th solution to Problem A

t = int(input())

def solve():
    d, n = map(int, input().split(' '))
    TIME = None
    for a1 in range(n):
        k, s = map(int, input().split(' '))
        if TIME is None or TIME < (d-k)/s:
            TIME = (d-k)/s
    return '{:.25}'.format(d/TIME)

for a0 in range(t):
    sol = solve()
    print("Case #" + str(a0 + 1) + ": " + sol)
