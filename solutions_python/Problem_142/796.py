import sys
import math
import collections
import itertools


TestCase = collections.namedtuple('TestCase', ['id', 'string'])


def read_line():
    return sys.stdin.readline().strip()


def read_inputs():
    n_tests = int(read_line())
    tests = []
    for case_id in range(1, n_tests + 1):
        strings = []
        n_strings = int(read_line())
        for _ in range(n_strings):
            strings.append(read_line())
        tests.append(TestCase(case_id, strings))

    return tests

def preprocess_strings(strings):
    # ['aab' 'abb'] -> [[('a', 2), ('b', 1)] ...]
    def prep_one(s):
        ans = []
        for k, g in itertools.groupby(s):
            ans.append((k, len(list(g))))
        return ans

    return [prep_one(x) for x in strings]

def solve(tid, strings):
    def format_answer(ans):
        return "Case #{}: {}".format(tid, ans)
    fw = 'Fegla Won'

    prepd = preprocess_strings(strings)
    if len(set(len(x) for x in prepd)) != 1:
        return format_answer(fw)

    trans = list(zip(*prepd))
    for r in trans:
        if len(set(x[0] for x in r)) != 1:
            return format_answer(fw)
    numbers = [[x[1] for x in r] for r in trans]
    def ops_per_letter(r):
        def f(c):
            return sum(abs(c - x) for x in r)
        goal = sum(r) / len(r)
        return min(f(x) for x in [math.ceil(goal), math.floor(goal)])

    ans = sum(ops_per_letter(r) for r in numbers)
    return format_answer(ans)



tcs = read_inputs()
for tc in tcs:
    print(solve(*tc))
