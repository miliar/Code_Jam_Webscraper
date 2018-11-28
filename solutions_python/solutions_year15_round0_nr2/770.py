#!/usr/bin/python
import sys
input_filename, = sys.argv[1:]
input = open(input_filename)
assert input_filename.endswith('.in'), input_filename
output = open(input_filename[:-3]+'.out', 'w')

T = int(input.readline())

def time(lst):
    if not lst:
        return 0
    lst = tuple(sorted(lst))
    t = time.cache.get(lst, None)
    if t is not None:
        return t
    assert lst[0] >= 1
    m = lst[-1]
    assert m > 0
    t = m
    for k in range(1, m//2 + 1):
        tt = 1 + time(lst[:-1] + (k, m - k))
        if tt < t:
            t = tt
    time.cache[lst] = t
    return t

time.cache = {}

def time_2(lst):
    if not lst:
        return 0
    lst = list(lst)
    lst.sort()
    assert lst[0] >= 1
    t1 = 1 + time_2([x-1 for x in lst if x>1])
    m = lst[-1]
    if m <= 1:
        return t1
    t2 = 1 + time_2(lst[:-1] + [m // 2, m - m//2])
    return min(t1, t2)

def solve():
    D = int(input.readline())
    lst = tuple(map(int,input.readline().strip().split()))
    assert len(lst) == D
    print lst
    t = time(lst)
    print '-->', t
    return t
        
for t in range(T):
    print >> output, 'Case #%s: %s' % (t+1,solve())
