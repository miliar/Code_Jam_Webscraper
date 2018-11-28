import sys

t = int(raw_input())

for i in range(0, t):
    raw = raw_input().split()
    m, s = int(raw[0]), raw[1]

    a = [int ( j ) for j in s]

    count = 0
    k = 0;
    for j in range(0, m + 1):
        if j > k:
            count += j - k
            k = j
        k += a[j]

    print "Case #" + str(i + 1) + ": " + str(count)
    #print m, a