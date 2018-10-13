import sys
from collections import defaultdict


def solve(stalls, people):
    """
    >>> solve(4, 2)
    (1, 0)
    >>> solve(5, 2)
    (1, 0)
    >>> solve(6, 2)
    (1, 1)
    >>> solve(1000, 1000)
    (0, 0)
    >>> solve(1000, 1)
    (500, 499)
    >>> solve(10, 1)
    (5, 4)
    >>> solve(10, 2)
    (2, 2)
    >>> solve(10, 3)
    (2, 1)
    >>> solve(10, 4)
    (1, 0)
    >>> solve(10, 5)
    (1, 0)
    >>> solve(10, 6)
    (1, 0)
    >>> solve(10, 7)
    (0, 0)
    >>> solve(10, 8)
    (0, 0)
    >>> solve(10, 9)
    (0, 0)
    >>> solve(10, 10)
    (0, 0)
    """
    variants = defaultdict(int)
    variants[stalls] = 1
    min_dist = max_dist = 0
    while people > 0:
        old_dist = max(variants)
        new_dist, new_offset = divmod(old_dist - 1, 2)
        min_dist, max_dist = new_dist, new_dist + new_offset
        if max_dist == 0:
            break
        count = variants.pop(old_dist)
        variants[min_dist] += count
        variants[max_dist] += count
        people -= count
    return max_dist, min_dist


def main():
    count = int(next(sys.stdin).strip())
    for case in xrange(1, count + 1):
        stalls, people = map(int, next(sys.stdin).split())
        print 'Case #{}: {} {}'.format(case, *solve(stalls, people))



if __name__ == '__main__':
    main()
