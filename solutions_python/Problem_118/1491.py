import sys
import math


def check_fair(num):
    strn = str(num)
    if strn == strn[::-1]:
        return True
    return False

def check_square(num):
    sq = math.sqrt(num)
    if sq > int(sq):
        return False
    else:
        return check_fair(int(sq))

input = sys.argv[1]
with open(input) as f:
    lines = f.readlines()
size = int(lines[0])
lines = lines[1:]
for i, line in enumerate(lines):
    ret = 0
    interval = [int(n) for n in line.split()]
    for j in xrange(interval[0], interval[1] + 1):
        if check_fair(j) and check_square(j):
            ret += 1
    print "Case #" + str(i+1) + ": " + str(ret)