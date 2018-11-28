import sys
import math

t = int(raw_input())

for i in range(0, t):
    s = raw_input().split()
    x, r, c = int(s[0]), int(s[1]), int(s[2])

    #print x, r, c

    a = math.ceil(math.sqrt(x))

    result = ''

    if (a > r or a > c) and a != x:
        print "Case #" + str(i + 1) + ": " + 'RICHARD'
        continue

    if (a >= r or a >= c) and x != 3 and a != x:
        print "Case #" + str(i + 1) + ": " + 'RICHARD'
        continue

    elif r*c%x ==0:
        result = 'GABRIEL'
    else:
        result = 'RICHARD'
    print "Case #" + str(i + 1) + ": " + result

    # if (a  >= r or a >= c) and a != x:
    #     print "Case #" + str(i + 1) + ": " + 'RICHARD'
    #     continue
    # if (a == r or )