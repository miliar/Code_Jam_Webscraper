def solve(c, f, x):
    sfarming = 0
    cps = 2.0
    best = x / 2
    while True:
        purchase = c / cps
        cps += f
        nextbest = sfarming + purchase + x / cps
        if nextbest >= best:
            return best
        best = nextbest
        sfarming += purchase

t = int(input())
for case in range(t):
    line = input().split(' ')
    c = float(line[0])
    f = float(line[1])
    x = float(line[2])
    print("Case #%d:" % (case+1), solve(c, f, x))

