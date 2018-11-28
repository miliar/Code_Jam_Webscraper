from __builtin__ import xrange


def left_s(stall, pos):
    for i in xrange(pos, 0, -1):
        if stall[i] == 1:
            return pos - i - 1
    return pos - 1

def right_s(stall, pos):
    length = len(stall)
    for i in xrange(pos, length):
        if stall[i] == 1:
            return i - pos - 1
    return i - 1

def print_stall(stall):
    for i in stall:
        if i == 1:
            print 0,
        if i == 0:
            print '.',
    print

def get_lrs(stalls):
    length = len(stalls)
    lr = []
    for i in xrange(length):
        if stalls[i] == 0:
            l = left_s(stalls, i)
            r = right_s(stalls, i)
            lr.append((i - 1, (l, r)))
    return lr

def occupy(lr, stalls, last=False):
    cord = [x[1] for x in lr]
    mins = [min(x) for x in cord]
    max_min = max(mins)
    if mins.count(max_min) <= 1:
        position = lr[mins.index(max_min)][0]
    else:
        to_add = []
        for i, _min in enumerate(mins):
            if _min == max_min:
                to_add.append(lr[i])
        # print 'to_add->', to_add
        cord1 = [x[1] for x in to_add]
        maxes = [max(x) for x in cord1]
        max_max = max(maxes)
        position = to_add[maxes.index(max_max)][0]
    stalls[position + 1] = 1
    return stalls[:], position

def solve(stalls, ppl):
    # print_stall(stalls)cd
    for i in xrange(ppl):
        lr = get_lrs(stalls)
        stalls, pos = occupy(lr, stalls)
        # print pos
        # print_stall(stalls)
    _full = all([x == 1 for x in stalls])
    if _full:
        # print 'FULL'
        return '0 0'
    for x in lr:
        if x[0] == pos:
            return '{} {}'.format(x[1][1], x[1][0])

i = 1
for test in range(int(raw_input().strip())):
    num_stalls, people = map(int, raw_input().strip().split())
    stalls = [0 for x in range(num_stalls)]
    stalls.insert(0, 1)
    stalls.append(1)
    print 'Case #{}: {}'.format(i, solve(stalls, people))
    i += 1