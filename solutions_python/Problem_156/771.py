import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
from collections import Counter

def potential_update(op):
    highest = max(op)
    second = highest / 2
    first = second + 1 if highest % 2 else second
    return highest, first, second


def shall_split(op, debug):
    highest, first, second = potential_update(op)
    right = sum([x[1] for x in op.iteritems() if x[0] > first])
    if debug:
        print (highest - first) > right, (highest, first, second), right, op
    if (highest - first) > right:
        return True

    # keys = op.keys()
    # if len(keys) > 1:
    #     if max(op) - max([p for p in op if p != max(op)]) > 1:
    #         return True


def split(op, highest, first, second):
    op[highest] -= 1
    if not op[highest]:
        op.pop(highest)
    op[first] += 1
    op[second] += 1

def zero_b(time, op, debug=False):
    current_max = max(op)
    split_res_tricky = None
    if current_max == 1:
        return time + 1
    highest, first, second = potential_update(op)
    if debug:
        oop = op.copy()
    if highest == 9:
        oop_tricky = op.copy()
        split(oop_tricky, 9, 6, 3)
        split_res_tricky = zero_b(time + 1, oop_tricky, debug)
    split(op, highest, first, second)
    split_res = zero_b(time + 1, op, debug)
    if debug:
        print 't:%s, max:%s, rec:%s, out:%s, inp:%s' % (time, current_max, split_res, time + min(split_res, current_max), oop)
    to_compare = [split_res, current_max + time]
    if split_res_tricky:
        to_compare.append(split_res_tricky)
    return min(to_compare)

def read_input():
    name = 'B-small-attempt3'
    f = open('%s.in' % name)
    f2 = open('%s.out' % name, 'w')
    num_cases = int(f.readline().replace('\n', ''))
    for i in xrange(num_cases):
        f.readline()
        case_input = [int(a) for a in f.readline().replace('\n', '').split(' ')]
        op = Counter(case_input)
        f2.write('Case #%s: %s\n' % (i + 1, zero_b(0, op)))
        # print case_input, zero_b(0, op)
        # import ipdb; ipdb.set_trace()


def test(expected, input, debug=False):
    op = Counter(input)
    print 'exp %s, got %s for %s' % (expected, zero_b(0, op), input)
    op = Counter(input)
    assert zero_b(0, op, debug) == expected

read_input()

test(2, [2])
test(3, [4])
test(5, [8])
test(5, [9])
test(6, [9, 6])
test(6, [9, 5, 5])
# test(7, [15])

test(6, [9, 6])

test(2, [1, 2])
test(3, [1, 4], False)

test(7, [1, 2, 3, 4, 5, 6, 7])

test(4, [4, 4, 4, 4])
test(7, [4, 8, 8, 8], False)
test(8, [8, 8, 8, 8])
test(9, [8, 8, 16])
test(10, [16, 16])
test(11, [32])

test(12, [33])

test(7, [16])
test(6, [8, 8])
test(6, [7, 7], False)
test(7, [5, 5, 5, 5, 5, 11, 1])

test(6, [5, 6, 4, 3, 4, 4, 5, 4, 6, 5, 1])
test(7, [5, 6, 7, 4, 4, 5, 4, 6, 5, 1])
test(8, [5, 6, 7, 8, 5, 4, 6, 5, 1])
test(9, [5, 6, 7, 8, 9, 6, 5, 1])
test(10, [5, 6, 7, 8, 9, 11, 1])

test(5, [5, 5, 5, 5, 5, 4, 3, 1])
test(6, [5, 5, 5, 5, 5, 7, 1])
test(7, [5, 5, 5, 5, 5, 7, 7, 1])
test(7, [5, 5, 5, 5, 5, 7, 7, 7, 1])

test(7, [5, 5, 5, 5, 8, 8, 1])
test(7, [5, 5, 5, 5, 8, 7, 1])

test(6, [5, 5, 5, 5, 5, 10, 1])
test(6, [5, 5, 5, 5, 5, 6])
test(5, [5, 5, 5, 5, 5])
test(6, [10, 4])
test(3, [1, 4])
test(3, [3])
test(3, [4])
test(3, [1, 4])

test(8, [5, 5, 8, 7, 10])
test(9, [5, 5, 8, 7, 16])
test(8, [4, 4, 8, 16])
test(12, [4, 4, 14, 16, 16, 16])
test(8, [3, 6, 6, 6, 9, 9])

test(20, [32, 32, 32, 32])
test(21, [33, 31, 33, 31])

test(15, [64])
test(16, [25, 39])

test(5, [9])
test(10, [1, 16, 16])
test(11, [1, 15, 17])
