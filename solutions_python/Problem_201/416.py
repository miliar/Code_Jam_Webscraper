#!/usr/bin/env python

from sys import stdin, stdout


def solve(n, k):
    i = 0
    p = 0
    while p < k :
        prev = p
        p += 2 ** i
        i += 1
    small_bucket_size, large_buckets = divmod(n-prev, prev+1)
    if (k - prev) <= large_buckets:
        # k-th people goes to a large 'bucket'
        free = small_bucket_size
    else:
        free = small_bucket_size - 1
    min_free = free // 2
    if (free % 2) == 0:
        return 2 * [min_free]
    else:
        return min_free + 1, min_free


cases = int(stdin.readline())
for case in range(cases):
    n, k = (int(_) for _ in stdin.readline().split())
    res = solve(n, k)
    stdout.write("Case #%d: %d %d\n" % (case+1, res[0], res[1]))
