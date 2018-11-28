import sys
import itertools

def uniq_ordered_chars(s):
    """
    "aabbbc" -> ["a", "b", "c"]
    """
    result = []
    for c in list(s):
        if not result or result[-1] != c:
            result.append(c)
    return result

assert uniq_ordered_chars("aabbbc") == ["a", "b", "c"]

def count_chars(s):
    """
    "aabbbc" -> [['a', 2], ['b', 3], ['c', 1]]
    """
    result = []
    for c in list(s):
        if not result or result[-1][0] != c:
            result.append((c, 1))
        else:
            result[-1] = (result[-1][0], result[-1][1] + 1)
    return result

assert count_chars("aabbbc") == [("a", 2), ("b", 3), ("c", 1)]

def calc_steps(f, t):
    if f == t:
        return 0
    else:
        steps = 0
        for i in xrange(0, len(f)):
            steps += abs(f[i][1] - t[i][1])
        return steps

sample_count = int(raw_input())
for i in xrange(1, sample_count + 1):
    print 'Case #%d:' % i,
    N = int(raw_input())
    str_list = [raw_input() for _ in xrange(0, N)]
    strs = set(str_list)
    if len(strs) == 1:
        print 0
    elif len(set(tuple(uniq_ordered_chars(s)) for s in strs)) != 1:
        print 'Fegla Won'
    else:
        uniq_chars = uniq_ordered_chars(str_list[0])
        uniq_char_count = len(uniq_ordered_chars(str_list[0]))
        strs_with_count = set([tuple(count_chars(s)) for s in strs])
        min_steps = sys.maxint
        for goal in strs_with_count:
            steps = 0
            for other in strs_with_count:
                steps += calc_steps(goal, other)
            if steps < min_steps:
                min_steps = steps
        print min_steps
