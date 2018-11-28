import sys

x = int(sys.stdin.readline())

d1 = "abcdefghijklmnopqrstuvwxyz "
d2 = "ynficwlbkuomxsevzpdrjgthaq "

d = {}

for i in range(len(d1)):
    d[d2[i]] = d1[i]

case = 1

for line in sys.stdin:
    s = "Case #" + str(case) + ": " 
    for c in line:
        s += d.get(c,c)
    sys.stdout.write(s)
    case = case + 1
