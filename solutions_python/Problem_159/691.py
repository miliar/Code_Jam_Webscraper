import sys
from math import ceil


def method1(mushrooms):
    total = 0
    for i in xrange(1, len(mushrooms)):
        if (mushrooms[i] - mushrooms[i-1]) < 0:
            total += abs(mushrooms[i] - mushrooms[i-1])
    return total

def method2(mushrooms):
    max_diff = 0
    for i in xrange(1, len(mushrooms)):
        ate = mushrooms[i] - mushrooms[i-1]
        if ate < 0 and abs(ate) > max_diff:
            max_diff = abs(ate)

    max_rate = max_diff / 10.0
    total = 0
    for x in mushrooms[:-1]:
        # print max_rate*10, x
        ate = min(max_rate*10, x)
        total += ate

    return total


with open(sys.argv[1], 'r') as input:
    num_cases = int(input.readline())
    f_out = open('mushrooms.out', 'w+')
    for k in xrange(1, num_cases+1):
        input.readline()
        mushrooms = [int(x) for x in input.readline().strip('\n').split(' ')]
        f_out.write('Case #%d: %d %d\n' % (k, method1(mushrooms), method2(mushrooms)))

    f_out.close()


