#!/usr/bin/python3

from sys import argv

class walk:
    def __init__(self, l, w):
        self.l, self.w = l, w
    def __lt__(self, other):
        return self.w < other.w

infile = open(argv[1])
cases = int(infile.readline())
for i in range(cases):
    x, s, r, t, n = map(int, infile.readline().split())
    w, e = [], []
    walkways = 0
    for j in range(n):
        bi, ei, wi = map(int, infile.readline().split())
        if j > 0 and bi < e[j-1]:
            print('Out of order!')
        if bi > x:
            print('Throw away walkway!')
            continue
        if ei > x:
            print('Walkway extends past x!')
            continue
        w.append(walk(ei-bi, wi))
        e.append(ei)
        walkways += ei - bi
    w.sort()
    # print('Walkways by ascending speed:')
    # for wj in w:
    #     print(wj.w)
    # run as much as possible when not on walkways
    # run on the slowest walkways the most? - sort!
    t1 = min(t, (x - walkways) / r)
    t2 = t - t1 # time for running on walkways
    # time for running on ground
    time = t1
    # time for walking on ground
    time += ((x - walkways) - t1 * r) / s
    # run on walkways as much as possible
    for wj in w:
        distance = wj.l
        if distance / (r + wj.w) <= t2:
            time += distance / (r + wj.w)
            t2 -=   distance / (r + wj.w)
        else:
            time += t2
            time += (distance - t2 * (r + wj.w)) / (s + wj.w)
            t2 = 0
    # pos = 0
    # time = 0
    # running1 = 0
    # running2 = 0
    # for j in range(len(b)):
    #     distance = b[j] - pos
    #     if running1 + distance / r <= t1:
    #         time += distance / r
    #         running1 += distance / r
    #     else:
    #         time += t1 - running1
    #         time += (distance - (t1 - running1) * r) / s
    #         running1 = t1
    #     pos = b[j]
    #     distance = e[j] - pos
    #     if running2 + distance / (r + w[j]) <= t2:
    #         time += distance / (r + w[j])
    #         running2 += distance / (r + w[j])
    #     else:
    #         time += t2 - running2
    #         time += (distance - (t2 - running2) * (r + w[j])) / (s + w[j])
    #         running2 = t2
    #     pos = e[j]
    # distance = x - pos
    # if running1 + distance / r <= t1:
    #     time += distance / r
    #     running1 += distance / r
    # else:
    #     time += t1 - running1
    #     time += (distance - (t1 - running1) * r) / s
    #     running1 = t1
    print('Case #{}: {}'.format(i+1, time))
