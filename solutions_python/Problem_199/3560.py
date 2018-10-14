#!usr/bin/python

import re

def negate(a):
    return "+" if a == "-" else "-"

n = int(raw_input())

for line in range(n):

    flips = 0
    cakes, size = str(raw_input()).split(" ")
    cakes = [str(i) for i in cakes]
    size = int(size)
    #print str(size) + " |",

    for char in range(len(cakes) - (size - 1)):
        if cakes[char] == "-":
            #cakes[char] = "(-)"
            for i in range(size):
                cakes[char + i] = negate(cakes[char + i])
            flips += 1

        #print cakes[char],

    if re.search("-", "".join(cakes)):
        print "Case #" + str(line + 1) + ": IMPOSSIBLE"
    else:
        print "Case #" + str(line + 1) + ": " + str(flips)

