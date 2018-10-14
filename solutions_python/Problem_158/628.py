def solve():
    x, r, c = list(map(int, input().split()))
    if r > c:
        r, c = c, r
    if (r*c % x):
        return "RICHARD"
    if (x == 1):
        return "GABRIEL"
    if (x == 2):
        return "GABRIEL"
    if (r == 1):
        return "RICHARD"
    if (x == 3):
        return "GABRIEL"
    if (r == 2):
        return "RICHARD"
    return "GABRIEL"

T = int(input())

for test in range(T):
    print("Case #%d: %s" % (test+1, solve()))
