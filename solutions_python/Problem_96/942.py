#!/usr/bin/python

# usage ./p2.py <input file>

import sys

def highestnum(n, surprize = False):
    if n <= 1:
        return n

    mod1 = (n % 3 == 1)
    mod2 = (n % 3 == 2)
    highest = n//3
    if surprize:
        if mod1:
            highest += 1
        elif mod2:
            highest += 2
        else:
            highest += 1
    else:
        if mod1 or mod2:
            highest += 1
    return highest


lines = open(sys.argv[1]).read().split("\n")

i=0

for line in lines[1:-1]:
    i += 1
    nums = line.split(" ")
    a = []
    for num in nums:
        a.append(int(num))
    #print "considering", a
    surcount = a[1]
    high = a[2]
    highcount = 0

    for n in a[3:]:
        if highestnum(n) >= high:
            highcount += 1
        elif surcount and highestnum(n, True) >= high:
            highcount += 1
            surcount -= 1
    print "Case #%d:" % i, highcount

#for num in (29,20, 8, 18, 18, 21, 0, 1, 2, 3, 4, 5):
#    print num, ":", highestnum(num), highestnum(num, True)

