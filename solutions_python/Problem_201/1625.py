from heapq import *

def cut(dis):
    r = dis-1
    half = r>>1
    if r % 2:
        return (half, half + 1)
    return (half, half)

def Solution(label, line):
    dis, count = map(lambda a: int(a), line.split())
    if count * 3 / 2.0 > dis:
        print "Case #{}: {} {}".format(label, 0, 0)
        return 1
    pool = []
    i = 0
    heappush(pool, -dis)
    l, r = None, None
    while i < count:
        largestDis = -heappop(pool)
        l, r = cut(largestDis)
        if l != 0:
            heappush(pool, -l)
        if r != 0:
            heappush(pool, -r)
        i += 1

    print "Case #{}: {} {}".format(label, r, l)
    return 1

if __name__ == '__main__':
    import sys

    file_name = sys.argv[1]
    with open(file_name) as f:
        line = f.readline()
        for i in xrange(1, int(line)+1):
            line = f.readline().strip('\n')
            out = Solution(i, line)