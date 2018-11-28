from UserString import *

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    input = raw_input().split(" ")
    s = input[0]
    mutable = MutableString(s)
    k = int(input[1])
    j = 0
    count = 0
    while j < len(mutable):
        while j < len(mutable) and mutable[j] != '-':
            j = j + 1
        if j == len(mutable):
            break
        if j + (k-1) < len(mutable):
            x = 0
            while x < k:
                if mutable[j+x] == '-':
                    mutable[j+x] = '+'
                else:
                    mutable[j+x] = '-'
                x = x + 1
            count = count + 1
        else:
            count = -1
            break
        j = j + 1
    if count == -1:
        print "Case #{}: IMPOSSIBLE".format(i)
    else:
        print "Case #{}: {}".format(i, count)
