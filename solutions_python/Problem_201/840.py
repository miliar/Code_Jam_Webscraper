''' google codejam 2017.C '''

from heapq import heappush, heappop

def solve(stalls, num):
    '''main solve function'''
    # just a hystogram: size => amount
    intervals = dict()
    # minheap, so we'll use negative numbers
    sizes = list()

    # initial state
    intervals[stalls] = 1
    heappush(sizes, -stalls)

    def add(size, amnt):
        '''adds intervals to our consideration set'''
        if size in intervals:
            intervals[size] += amnt
        else:
            heappush(sizes, -size)
            intervals[size] = amnt

    while num > 0:
        # pull amnt biggest intervals
        size = -heappop(sizes)
        amnt = intervals[size]
        del intervals[size]
        # split into smaller ones
        size1 = size // 2
        size2 = (size-1) // 2
        # add smaller to the queue
        add(size1, amnt)
        add(size2, amnt)
        num -= amnt
        if num <= 0:
            return (size1, size2)

cases_amnt = int(raw_input())  # read a line with a single integer
for i in xrange(1, cases_amnt + 1):
    n, m = [int(s) for s in raw_input().split(" ")]
    [s1, s2] = solve(n, m)
    print "Case #{}: {} {}".format(i, s1, s2)
