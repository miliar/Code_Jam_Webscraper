#!/usr/bin/python

f = open("C-small-attempt0.in", "r")
out = open("C-small.out", "w")

T = int(f.readline())

def ispal(n):
    return str(n) == str(n)[::-1]

for i in range(T):
    A, B = [int(n) for n in f.readline().split()]

    count = 0
    for n in range(A, B+1):
        if ispal(n):
            sq = n ** 0.5
            if sq % 1 == 0 and ispal(int(sq)):
                count += 1

    out.write("Case #%d: %d\n" % (i+1, count))

out.close()
f.close()

