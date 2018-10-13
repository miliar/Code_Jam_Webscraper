import math

for t in range(input()):
    print "Case #%s:" % str(t + 1),
    r, t = map(int, raw_input().split())
    i = int((math.sqrt((2 * r - 1) ** 2 + 8 * t) - 2 * r + 1) / 4.0)
    while i *(2*i+2*r-1) > t: #correct floating point operation error
        i -= 1
    print i
