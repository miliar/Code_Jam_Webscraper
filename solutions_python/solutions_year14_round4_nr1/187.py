from bisect import bisect


def to_ints(s):
    return map(int, s.split())


def get_ints():
    return to_ints(raw_input())

n_cases = input()

for case in xrange(1, n_cases + 1):
    file_count, capacity = get_ints()
    sizes = get_ints()

    cd_count = 0

    sizes.sort()

    while sizes:
        cd_count += 1
        first = sizes.pop()
        remaining = capacity - first
        point = bisect(sizes, remaining)
        if point > 0:
            sizes.pop(point-1)

    print "Case #%d: %s" % (case, cd_count)
