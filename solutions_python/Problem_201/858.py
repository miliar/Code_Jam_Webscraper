debug = False
import heapq

def split(n):
    if n % 2 == 0:
        return (n / 2 - 1, n / 2)
    else:
        return (n / 2, n / 2)

def heappush(h, N, x):
    heapq.heappush(h, (N - x, x))

def heappop(h): 
    (_, x) = heapq.heappop(h)
    return x

def case(N, K):
    if debug: print "----"
    if debug: print "N:", N, "K:", K
    h = []
    heappush(h, N, N)
    for i in range(K - 1):
        biggest_section = heappop(h)
        print biggest_section
        l, r = split(biggest_section)
        if debug: print l, r
        heappush(h, N, l)
        heappush(h, N, r)
        if debug: print h
    biggest_section = heappop(h)
    return split(biggest_section)

def add_count(counts, x, count):
    if x in counts:
        counts[x] += count
    else:
        counts[x] = count

def push(h, N, x, counts, count, s):
    if x > 0:
        if x not in s: 
            heappush(h, N, x)
            s.add(x)
        add_count(counts, x, count)

def fast_case_helper(N):
    h = []
    s = set()
    counts = dict()
    push(h, N, N, counts, 1, s)
    while h != []:
        x = heappop(h)
        count = counts[x]
        yield(count, x)
        # print "{} {}".format(count, x)
        if x % 2 == 0:
            push(h, N, x / 2 - 1, counts, count, s)
            push(h, N, x / 2, counts, count, s)
        else:
            push(h, N, x / 2, counts, count * 2, s)

def fast_case(N, K):
    if debug: print "----"
    if debug: print "N:", N, "K:", K
    count = 0
    size = -1
    y = fast_case_helper(N)
    while True:
        if debug: print "count:", count, "K:", K
        (c, size) = next(y)
        if debug: print "(c, size):", (c, size)
        count += c
        if count >= K:
            if debug: print "returning", size
            return split(size)
    #     print "count:", count
    # (c, size) = next(y)
    # print "size:", size

import fileinput
stdin = fileinput.input()
T = int(next(stdin))
print "T:", T

for n in range(1, T+1):
    input_ = next(stdin)
    input_ = input_.split(' ')
    N = int(input_[0])
    K = int(input_[1])
    z, y = fast_case(N, K)
    print "Case #{}: {} {}".format(n, y, z)
    # z, y = case(N, K)
    # print "Case #{}: {} {}".format(n, y, z)
