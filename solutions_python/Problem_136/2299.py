import sys
sys.setrecursionlimit(100000)
lines = open("B-large.in").read().split("\n")[1:]

c = 0
x = 0
f = 0
def solve(speed, aim):
    need = 0
    while aim > c:
        t1 = aim / speed
        t2 = c / speed + aim / (speed + f)
        if t1 < t2:
            break
        need += c / speed
        speed += f
    need += aim / speed
    return need

for i, line in enumerate(lines):
    if not line.strip():
        continue
    (c, f, x) = tuple([float(x) for x in line.split()])
    print "Case #%d:" % (i + 1), "%.7f" % solve(2, x)
