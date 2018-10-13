import collections


def _split(n):
    h1 = (n - 1) / 2
    return n - 1 - h1, h1


def solve(n, k):
    size_to_count = collections.Counter({n: 1})
    while k > 1:
        max_size = max(size_to_count)
        operations_to_perform = min(k - 1, size_to_count[max_size])
        h1, h2 = _split(max_size)
        size_to_count[h1] += operations_to_perform
        size_to_count[h2] += operations_to_perform
        size_to_count[max_size] -= operations_to_perform
        if size_to_count[max_size] == 0:
            del size_to_count[max_size]
        k -= operations_to_perform
    max_size = max(size_to_count)
    return _split(max_size)


if __name__ == '__main__':
    testcases = int(raw_input())
    for i in xrange(testcases):
        n, k = (int(x) for x in raw_input().split())
        y, z = solve(n, k)
        print 'Case #{}: {} {}'.format(i + 1, y, z)
