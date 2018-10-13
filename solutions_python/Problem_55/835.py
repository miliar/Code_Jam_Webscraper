# vim:fileencoding=utf-8

from __future__ import print_function

FEE = 1
def calc(r, k, line):
    sales = 0
    index = 0
    # roller coaster runs r times in a day
    for i in xrange(r):
        capacity = k
        group = 0
        n = len(line)
        onboard = 0
        while capacity >= 0 and onboard != n:
            group = line[index]
            capacity = capacity - group
            sales = sales + group
            onboard = onboard + 1
            if index + 1 < len(line):
                index = index + 1
            else:
                index = 0
        if capacity < 0:
            sales = sales - group
            index = index - 1
    print(sales)

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 1:
        print("[usage] %0 [input file]" % sys.argv[0])
        sys.exit(0)

    with open(sys.argv[1], 'r') as f:
        t = int(f.next().strip())
        for i in range(t):
            r, k, n = map(lambda e: int(e), f.next().strip().split())
            line = [int(x) for x in f.next().strip().split()]
            print("Case #%d:" % (i+1), end=" ")
            calc(r, k, line)
