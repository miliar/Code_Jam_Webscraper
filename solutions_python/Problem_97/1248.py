#!/usr/bin/python

def recycle(A, B):
    total = 0
    if A < 10 and B < 10:
        return total
    for n in range(A, B + 1):
        m = n
        for j in range(len(str(n))):
            m = int(str(m)[-1] + str(m)[0:-1])
            if m <= B and m > n and m >= A:
                total += 1
    return total

f = file('q3.in', 'r')

i = 0
for l in f:
    if i > 0:
        A = int(l.split(" ")[0])
        B = int(l.split(" ")[1])
        print "Case #%d: %d" % (i, recycle(A, B))
    i = i + 1

f.close()
