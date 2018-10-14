"""
Problem b
John S.
"""
import sys

inputfile = "B-large.in"
outputfile = "out_lrg.txt"
fi = open(inputfile)
g = open(outputfile, "ab")
t = int(fi.readline().strip())

for n in range(t):
    line = fi.readline().split()
    nl = [float(k) for k in line]
    c = nl[0] #farm cost
    f = nl[1] #farm output
    x = nl[2] #target cookies

    time = 0
    rate = 2
    total = 0
    while True:
        #calc time to farm
        ttf = c/rate
        #calc time to done
        ttd = x/rate

        if ttd <= ttf + x/(rate + f):
            time += ttd
            break
        else:
            time += ttf
            rate += f
    m = n+1

    outstr = "Case #" + str(m) + ": " + str(time) + "\n"
    sys.stdout.write(outstr)
    g.write(outstr.encode("ASCII"))