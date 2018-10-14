import math
import time

file = open("A-small-attempt0.in", "r")
outfile = open("output-attempt0.out", "w")

T = int(file.readline().strip())
for testcase in range(T):
    r, t = file.readline().strip().split()
    r, t = int(r), int(t)
    # first black ring around a white circle of radius r cm
    # starts with t millilitres of black paint
    
    drawed_rings = 0
    while True:
        required_paint = (r + 1) * (r + 1) - (r) * (r)
        if t < required_paint: break
        t -= required_paint
        drawed_rings += 1
        r += 2
    
    print "Case #%s: %s" % (testcase + 1, drawed_rings)
    outfile.write("Case #%s: %s\n" % (testcase + 1, drawed_rings))