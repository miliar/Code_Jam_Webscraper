
import sys
import math

ntests = int(sys.stdin.readline())

for ncase in range(ntests):
    N, K = map(int, sys.stdin.readline().split(' '))

    # print("## Starting case {0}".format(ncase + 1))

    sizes = { N: 1 }
    remaining = K

    while remaining > 0:

        def addToDict(d, key, num):
            if key not in d: d[key] = 0
            d[key] += num

        size = max(sizes.keys())
        count = sizes.pop(size)
        # for size, count in sorted(sizes.items(), key=lambda a:-a[0]):

        # do our injection of real persons
        # numToInsert = min(remaining, count)
        # if numToInsert == 0: break
        remaining -= min(remaining, count)

        # create new sizes
        newMin = math.floor((size - 1) / 2)
        newMax = math.ceil((size - 1) / 2)
        addToDict(sizes, newMin, count)
        addToDict(sizes, newMax, count)

        # print("inserting {0} (up to {1}) people into a width of {2} => [{3},{4}]".format(numToInsert, count, size, newMin, newMax))

    result = '{0} {1}'.format(newMax, newMin)

    print('Case #{0}: {1}'.format(ncase + 1, result))
