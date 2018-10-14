import sys
import string

filename = sys.argv[1]
f = open(filename, "r")
lines = map(string.strip, f.readlines())
T = int(lines[0])



def solve(x, r, c):
    if x == 1:
        return True
    elif x == 2:
        if (r * c) % 2 == 0:
            return True
        else:
            return False
    elif x == 3:
        if (r == 2 and c == 3) or \
               (r == 3 and c == 3) or \
               (r == 3 and c == 4):
            return True
        else:
            return False
    elif x == 4:
        if (r == 3 and c == 4) or \
               (r == 4 and c == 4):
            return True
        else:
            return False


for t in range(T):
    line = lines[t + 1]
    x, r, c = map(int, line.split())

    if c < r:
        c, r = r, c

    if solve(x,r,c):
        print "Case #%s: %s" % (t + 1, "GABRIEL")
    else:
        print "Case #%s: %s" % (t + 1, "RICHARD")
