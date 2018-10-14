#!/usr/bin/python
import fileinput


def untranslate(x):
    if x == 3:
        return 'i'
    if x == 5:
        return 'j'
    if x == 7:
        return 'k'
    raise Exception('can not translate %s' % x)


def translate(x):
    if x == 'i':
        return 3
    if x == 'j':
        return 5
    if x == 'k':
        return 7
    raise Exception('can not translate %s' % x)

#i = 3, j = 5, k = 7
seed_dict = {
    (1, None): 1,
    (3, None): 3,
    (5, None): 5,
    (7, None): 7,
    (None, 1): 1,
    (None, 3): 3,
    (None, 5): 5,
    (None, 7): 7,
    (1, 1): 1,
    (3, 1): 3,
    (5, 1): 5,
    (7, 1): 7,
    (1, 3): 3,
    (1, 5): 5,
    (1, 7): 7,
    (3, 3): -1,
    (5, 5): -1,
    (7, 7): -1,
    (3, 5): 7,
    (3, 7): -5,
    (5, 3): -7,
    (5, 7): 3,
    (7, 3): 5,
    (7, 5): -3,
}

final_dict = {}

for (a, b), v in seed_dict.iteritems():
    final_dict[(a, b)] = v
    if a is not None:
        final_dict[(-a, b)] = -v
    if b is not None:
        final_dict[(a, -b)] = -v
    if a is not None and b is not None:
        final_dict[(-a, -b)] = v


def get_cases():
    inp = fileinput.input()
    inp.next()
    for line in inp:
        _, repeat = map(int, line.strip().split())
        yield map(translate, list(inp.next().strip())) * repeat


def get_tail_matches(case):
    x = None
    for i in xrange(len(case) - 1, 1, -1):
        x = final_dict[(case[i], x)]
        if x == 7:
#            print 'tail', ''.join(map(untranslate, case[i:]))
            yield i


def get_head_matches(case):
    x = None
    for i in xrange(0, len(case)):
        x = final_dict[(x, case[i])]
        if x == 3:
#            print 'head', ''.join(map(untranslate, case[:i + 1]))
            yield i


def check_middle_match(case, start, tail_matches):
    x = None
    for i in xrange(start, max(tail_matches) + 1):
        x = final_dict[(x, case[i])]
        if x == 5:
            if i + 1 in tail_matches:
                return True
    return False


def solve(case):
#    print 'case', ''.join(map(untranslate, case))
    head_matches = list(get_head_matches(case))
#    print 'head', head_matches
    tail_matches = set(list(get_tail_matches(case)))
#    print 'tail', tail_matches
    if len(head_matches) == 0 or len(tail_matches) == 0:
        return False
#    print head_matches
#    print tail_matches
    for head_match in head_matches:
        if check_middle_match(case, head_match + 1, tail_matches):
            return True
    return False


if __name__ == '__main__':
    for num, case in enumerate(get_cases(), 1):
        print('Case #%d: %s' % (num, 'YES' if solve(case) else 'NO'))
