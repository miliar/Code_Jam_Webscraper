from sys import argv
import math

def get_answer(r1,r2,t, to_use, count):
    while True:
        if t >= to_use:
            count += 1
            t -= to_use
            r1 += 2
            r2 = r1 + 1
            to_use = (r2-r1)*(r2+r1)
        else:
            break
    return count
file = open(argv[1], 'r')
T = eval(file.readline())
i = 1
while T > 0:
    rt = map(int, file.readline().strip().split())
    r1 = rt[0]
    r2 = r1 + 1
    t = rt[1]
    to_use = (r2-r1)*(r2+r1)
    count = 0
    answer = get_answer(r1,r2,t, to_use, count)
    print "Case #%d: %d" % (i, answer)
    i += 1
    T -= 1
