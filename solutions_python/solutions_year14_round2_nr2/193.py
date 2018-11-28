import math
f = open('B-small-attempt0.in', 'r')
numCases = int(f.readline())
x = 1
while x <= numCases:
    line = f.readline()
    a, b, k = line.split()
    a, b, k = int(a), int(b), int(k)
    i = j = 0
    count = 0
    while i < a:
        j = 0
        while j < b:
            if (i & j) < k:
                count += 1
            j += 1
        i += 1
    print "Case #" + str(x) + ": " + str(count)
    x += 1