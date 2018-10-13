#! /usr/bin/env python
import sys
import math

sample = "sample"

if len(sys.argv) < 2:
    print "usage: %s [sample | name]" % (sys.argv[0], )
    sys.exit(1)

if sys.argv[1].lower() == "sample":
    fin = open(sample + ".in", "r") 
    fout = open(sample + ".out", "w")
else:
    fin = open(sys.argv[1], "r")
    fout = open(sys.argv[1] + ".out", "w")

case = 1
ncases = int(fin.readline())

def is_palindrome(num):
    num = str(num)
    l = len(num)
    mid = l / 2

    i = 0
    j = l - 1
    while i < mid:
        if num[i] != num[j]:
            return False
        i += 1
        j -= 1

    return True

while True:
    line = fin.readline()
    line = line.rstrip()

    parts = line.split()
    small = int(parts[0])
    big = int(parts[1])
    count = 0
    low = math.sqrt(small)
    low = int(math.ceil(low))
    high = math.sqrt(big)
    high = int(math.floor(high))

    for n in xrange(low, high + 1):
        if is_palindrome(n):
            s = n ** 2
            if is_palindrome(s):
                count += 1

    msg = "Case #%d: %d\n" % (case, count)
    print msg,
    fout.write(msg)
    matrix = []
    case += 1

    if case > ncases:
        break

fin.close()
fout.close()
