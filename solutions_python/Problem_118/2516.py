#!/usr/bin/env python

import math

fin = open("C-small-attempt0.in", "r")
data = fin.readlines()
fin.close()


def solve(start, end):
    result = []
    for i in range(start, end+1):
        # is it a palindrome?
        if str(i) == str(i)[::-1]:
            # yes

            # is it a square of a palindrome
            sqrt = math.sqrt(i)

            if (sqrt % 1) != 0.0:
                continue

            sqrt = int(math.floor(sqrt))
            if str(sqrt) == str(sqrt)[::-1]:
                #print "FS:",i,sqrt
                result.append(i)
    return len(result)

fout = open("C-small-attempt0.out", "w")

for i,case in enumerate(data[1:]):
    start, end = case.strip().split()
    result = solve(int(start), int(end))
    fout.write("Case #%d: %d\n" % (i+1,result))

fout.close()
