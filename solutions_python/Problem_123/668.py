#!/usr/bin/python3

import math

fi = open("/home/vadim/Downloads/a.txt", "r")
cn = int(fi.readline())
fo = open("/home/vadim/Downloads/b.txt", "w")

for cs in range(1, cn + 1):
    print("Case", cs)
    fo.write("Case #" + str(cs) + ": ")

    line = fi.readline().split()
    a = int(line[0])
    n = int(line[1])

    line = fi.readline().split()
    m = sorted([int(x) for x in line])

    if a == 1:
        print("count", n)
        fo.write(str(n) + "\n")
        continue

    print(a)
    print(m)

    size = a
    count = 0
    i = 0

    while i < n:
        if size > m[i]:
            size += m[i]
            i += 1
        else:
            z = size
            c = 0
            while z <= m[i]:
                c += 1
                z += (z - 1)
            if c > (n - i):
                count += n - i
                break
            count += 1
            size += (size - 1)

    print("count", count)
    fo.write(str(count) + "\n")

fi.close()
fo.close()
