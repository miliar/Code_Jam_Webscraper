# -*- coding: utf-8 -*-
# This library is available online and free to use:
# https://github.com/yanatan16/pycodejam
from codejam.parsers import iter_parser, ints

# Input
#
# 3
# 3 3
# 2 1 2
# 1 1 1
# 2 1 2
# 5 5
# 2 2 2 2 2
# 2 1 1 1 2
# 2 1 2 1 2
# 2 1 1 1 2
# 2 2 2 2 2
# 1 3
# 1 2 1

# Output
#
# Case #1: YES
# Case #2: NO
# Case #3: YES


def check_position(array, n, m, i, j):
    # check row
    row = m * i
    current = array[row + j]
    print 'row = ', row
    print 'i =', i, 'j =', j
    # import ipdb; ipdb.set_trace()
    # print array[row:row + j], array[row + j + 1:row + m], array[j::m], array[j::m][:i], array[j::m][i + 1:]
    row_prev = array[row:row + j]
    row_post = array[row + j + 1:row + m]
    col_prev = array[j::m][:i]
    col_post = array[j::m][i + 1:]
    if (row_prev and max(row_prev) > current or row_post and max(row_post) > current) and \
            (col_prev and max(col_prev) > current or col_post and max(col_post) > current):
        return False
    return True

    # check col

#     pattern = array[n * index:n * index + m]
#     # print 'cut_row', index, pattern, max(pattern), height
#     if max(pattern) > height:
#         return False
#     # print 'cut_row', lawn
#     lawn[n * index:n * index + m] = [height if i > height else i
#                                      for i in lawn[n * index:n * index + m]]
#     # print 'cut_row', lawn
#     return True
#
#
# def cut_column(lawn, array, n, m, index, height):
#     pattern = array[index::m]
#     # print 'cut_col', index, pattern, max(pattern), height
#     if max(pattern) > height:
#         return False
#     # print 'cut_col', lawn
#     lawn[index::m] = [height if i > height else i
#                       for i in lawn[index::m]]
#     # print 'cut_col', lawn
#     return True


def solve(*lines):
    n = len(lines)
    m = len(lines[0])
    array = tuple(reduce(lambda x, y: x + y, lines))
    print 'n =', n, ' m =', m
    for i in xrange(n):
        for j in xrange(m):
            if not check_position(array, n, m, i, j):
                return 'NO'
    return 'YES'

    # array = tuple(reduce(lambda x, y: x + y, lines))
    # nm = len(array)
    # heights = sorted(list(set(array)), reverse=True)
    # max_height = heights.pop(0)
    # # print heights
    # lawn = list(max_height for unused in array)
    # for height in heights:
    #     # print 'height', height
    #     for i in xrange(m):
    #         # top or down
    #         # print i, nm + i - m, (array[i], array[nm + i - m])
    #         # if height in (array[i], array[nm + i - m]):
    #         cut_column(lawn, array, n, m, i, height)
    #     for i in xrange(n):
    #         # left or right
    #         # print m * i, m * i + m - 1, (array[m * i], array[m * i + m - 1])
    #         # if height in (array[m * i], array[m * i + m - 1]):
    #         cut_row(lawn, array, n, m, i, height)
    #     for i in xrange(n):
    #         for j in xrange(m):
    #             # print i, j, (lawn[i * n + j], array[i * n + j])
    #             if lawn[i * n + j] > array[i * n + j] and array[i * n + j] == height:
    #                 return 'NO'
    # # print lawn
    # return 'YES'


# def iter_wrap(f):
#     def wrap():
#         return list(f())
#     return wrap


@iter_parser
def parse(nxtline):
    n, m = nxtline().split()
    return [map(int, nxtline().split()) for unused in xrange(int(n))]


if __name__ == "__main__":
    from codejam import CodeJam
    # import ipdb; ipdb.set_trace()
    CodeJam(parse, solve).main()
