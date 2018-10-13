#!/usr/bin/python

import re
import sys

def handle(target, n, indexes, test):

    # try to short-circuit early

    keys = indexes.keys()

    for x in keys:
        if x not in test:
            return 0

    test = ''.join(c for c in test if c in keys)

    start = test.find(target[0])
    if start > len(test) - n:
        return 0

    end = test.rfind(target[-1])
    if end < n - 1:
        return 0

    test = test[start:end + 1]
    if len(test) < n:
        return 0

    stats = {}

    for c in test:
        for index in indexes[c]:

            if index:
                pre = target[:index]
                if pre not in stats:
                    break

                pre_count = stats[pre]

                curr = target[:index + 1]
                stats[curr] = stats.get(curr, 0) + pre_count

            else:
                stats[c] = stats.get(c, 0) + 1

    return stats.get(target, 0)


def main():

    if len(sys.argv) < 2:
        print "need file"
        return
    
    target = 'welcome to code jam'
    targetn = len(target)

    indexes = {}
    for x in set(target):
        indexes[x] = [m.start() for m in re.finditer(x, target)]

    with open(sys.argv[1]) as file:
        N = int(file.readline())

        for n in xrange(N):
            count = str(handle(target, targetn, indexes, file.readline().rstrip()))
            print "Case #{0}: {1:0>4}".format(n + 1, count[-4:])


if __name__ == "__main__":
    main()

