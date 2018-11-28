import math
T = input()

for i in range(T):
    line = raw_input()
    r, t = map(int, line.split())

    paint = t
    result = 0
    black = (r+1)*(r+1)-r*r
    while paint >= 0:
        paint -= black
        black += 4
        result += 1

    print "Case #%d: %d" % (i+1, result-1)
