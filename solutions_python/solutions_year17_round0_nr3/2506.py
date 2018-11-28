import math
import os
import time

__author__ = 'ricky'


def stalls(N, K):
    vals = {}
    i1 = 0
    i2 = 0
    for i in range(0, K):
        if len(vals) == 0:
            num = N
        else:
            num = max(vals)
            idx = vals[num]
            vals[num] = idx - 1
            if idx == 1:
                vals.pop(num)
        mid = math.ceil(num / 2)
        i1 = mid - 1
        i2 = num - mid
        add_to_dict(vals, i1)
        add_to_dict(vals, i2)

    return max(i1, i2), min(i1, i2)


def add_to_dict(vals, i):
    try:
        vals[i] += 1
    except KeyError:
        vals[i] = 1


def read_file(input):
    i = 0
    lines = (line.rstrip('\n') for line in open(input))
    for xx in lines:
        i += 1
        if i == 1:
            continue
        arr = xx.split()
        res = stalls(int(arr[0]), int(arr[1]))
        yield ('Case #{}: {}'.format(i - 1, " ".join(map(str, res))))


if __name__ == '__main__':

    start = time.clock()
    with open('sample-data/C-small-2-attempt1.out', 'w') as the_file:
        for line in (read_file('sample-data/C-small-2-attempt1.in')):
            the_file.write(line + os.linesep)
    end = time.clock()
    print("%.2gs" % (end - start))
