import math
import re

fp = open('A-large.in')

cases = int(fp.readline())
case = 0

for case in range(0, cases):
    line = map(int, fp.readline().split(" "))
    maxPerKey = line[0]
    numKeys = line[1]
    alpha = line[2]
    freq = map(int, fp.readline().split(" "))
    freq.sort(cmp)
    freq.reverse()
    
    keys = [0] * numKeys # num of letters currently assigned to the key
    pressed = 0
    for f in freq:
        keys.sort()
        keys[0] += 1
        pressed += (keys[0] * f)

    print "Case #%i: %i" % (case + 1, pressed)

fp.close()
