#! /bin/python

fd = open("result.txt", "r")

r = 0
n = 1

for l in fd.readlines():
    if 0 == r:
        r = r + 1
        continue

    print "Case #%d: %s" % (n, l),
    n = n + 1
