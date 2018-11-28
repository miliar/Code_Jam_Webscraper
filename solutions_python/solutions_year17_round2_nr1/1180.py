from __future__ import division
f = open("A-large.in")
out = open("output.txt", "w")
t = int(f.readline().strip())
tt = 1
while tt <= t:
    hDisSpeed = []
    d, h = map(int, f.readline().strip().split())
    while h > 0:
        dStart, speed = map(int, f.readline().strip().split())
        hDisSpeed.append((d-dStart)/speed)
        h -= 1
    print hDisSpeed
    hDisSpeed.sort(reverse=True)
    out.write("Case #" + str(tt) + ": " + "{0:.6f}".format(d/hDisSpeed[0]) + "\n")
    tt += 1
