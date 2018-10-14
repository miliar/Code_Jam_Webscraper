import os
lines = [ x for x in open(os.path.dirname(__file__) + "/input.txt") ][1:]
for i, line in enumerate(lines):
    n, k = [ int(x) for x in line.split() ]
    t = 2 ** n
    k += 1
    if k % t == 0:
        light = "ON"
    else: light = "OFF"
    print "Case #%i: %s" % (i + 1, light or "OFF")