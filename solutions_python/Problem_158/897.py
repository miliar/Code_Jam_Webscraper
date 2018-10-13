import sys
import math

def p(*m):
    print(*m, file=sys.stderr)

liste = list()
with open(sys.argv[1]) as f:
    for i, l in enumerate(f.readlines()):
        l = l[:-1]
        if i == 0:
            t = int(l)
        else:
            liste.append([int(x) for x in l.split()])

solutions = list()
for s in liste:
    x, r, c = s
    p(x, r, c)
    if (r * c) % x != 0:
        solutions.append("RICHARD")
    elif min(r, c) < math.ceil(x/2):
        solutions.append("RICHARD")
    elif x != 2 and x % 2 == 0 and min(r, c) == math.ceil(x/2):
        solutions.append("RICHARD")
    else:
        solutions.append("GABRIEL")

for i, s in enumerate(solutions):
    print("Case #{}: {}".format(i + 1, s))
