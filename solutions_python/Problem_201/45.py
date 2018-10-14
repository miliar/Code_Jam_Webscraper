import sys
import heapq
import weakref
import codejam


class SpaceCountEntry(object):
    __slots__ = 'space', 'count'

    def __init__(self, space, count):
        self.space = space
        self.count = count


def split_space(space):
    left = (space - 1) // 2
    right = space - left - 1
    return left, right


def find_space_for_nth(n, num_stalls):
    counts = {}
    spaces = []

    def get():
        return -heapq.heappop(spaces)

    def inc(_space, _count):
        if _space in counts:
            counts[_space] += _count
        else:
            heapq.heappush(spaces, -_space)
            counts[_space] = _count

    inc(num_stalls, 1)

    while True:
        space = get()
        assert space >= 1
        count = counts.pop(space)
        if count >= n:
            return space
        n -= count
        left_space, right_space = split_space(space)
        inc(left_space, count)
        inc(right_space, count)


def format_result(n, num_stalls):
    space = find_space_for_nth(n, num_stalls)
    l, r = split_space(space)
    return '{} {}'.format(max([l, r]), min([l, r]))


def parser(reader):
    num_stalls, n = reader.readline().split()
    return format_result(int(n), int(num_stalls))


if __name__ == '__main__':
    codejam.run(parser, open('bathroom-large.in', 'r'), open('bathroom-large.out', 'w'))
