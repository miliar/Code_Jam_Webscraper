#!/usr/bin/python
import sys
with open('game.txt') as f:
    content = f.readlines()
content = map(lambda s: s.strip(), content)
content = filter(None, content)
case = 1
for line in content:
    CpS = 2.00000
    sum_bfarm = 0.000000
    floats = [float(i) for i in line.split()]
    C,F,X = floats[0],floats[1],floats[2]
    time = X/CpS
    while True:
        bfarm = C/CpS
        sum_bfarm += bfarm
        CpS += F
        if ((X/CpS) + sum_bfarm > time):
            break
        else:
            time = (X/CpS) + sum_bfarm
    sys.stdout.write("Case #%d: %.07f\n" % (case,time))
    case += 1
