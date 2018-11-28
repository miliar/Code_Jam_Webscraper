import os
import time
import unittest
from contextlib import contextmanager


PROB_NAME = 'repeater'
INPUT_TYPE = 'small'


def count_repeating(word):
    current_char = word[0]
    current_count = 1
    count = []
    for char in word[1:]:
        if char == current_char:
            current_count += 1
        else:
            count.append((current_char, current_count))
            current_char = char
            current_count = 1
    count.append((current_char, current_count))
    try:
        current_char = char
    except UnboundLocalError:
        current_char = word[0]
    current_count = 1
    return count


def solve(case):
    """break 'case', solve and return the solution"""
    words = case
    counts = [count_repeating(word) for word in words]
    l = len(counts[0])
    for count in counts:
        if len(count) != l:
            return "Fegla Won"
    changes = 0
    for i in range(l):
        char_counts = []
        for count in counts:
            if count[i][0] != counts[0][i][0]:
                return "Fegla Won"
            char_counts.append(count[i][1])
        average = int(round(sum(char_counts) / float(len(words))))
        for char_count in char_counts:
            changes += abs(char_count - average)
    return changes


def read_case(lines):
    word_num = int(lines.pop(0).strip())
    return [lines.pop(0).strip() for _ in range(word_num)]


def read_file(filepath):
    """Read the input file and return a list of cases in a tuple format."""
    cases = []
    with open(filepath, 'rt') as fobj:
        lines = fobj.readlines()
        num_cases = int(lines.pop(0))
        for _ in range(num_cases):
            cases.append(read_case(lines))
    return cases


def write_results(results, outfile):
    with open(outfile, 'wt') as f:
        for idx, result in enumerate(results):
            f.write('Case #{}: {}\n'.format(idx + 1, result))


@contextmanager
def timing(prefix):
    start = time.time()
    yield
    print '{} took {} seconds.'.format(prefix, time.time() - start)


def main(infile, outfile):
    cases = read_file(infile)
    results = []
    for idx, case in enumerate(cases):
        with timing("Solving case #{}".format(idx)):
            results.append(solve(case))
    write_results(results, outfile)


class UnitTest(unittest.TestCase):
    CASES = {('maw', 'mmaw'): 1,
             ('gcj', 'cj'): 'Fegla Won',
             ('aaabbb', 'ab', 'aabb'): 4,
             ('abc', 'abc'): 0,
             ('aabc', 'abbc', 'abcc'): 3}

    def runTest(self):
        message = 'Wrong result for case.\nCase: {}\nResult: {}\n'\
                  'Expected result: {}'
        for case, result in self.CASES.iteritems():
            self.assertEqual(solve(case), result, message.format(case,
                                                                 solve(case),
                                                                 result))

if __name__ == '__main__':
    assert len(UnitTest.CASES) > 0, "Don't be an idiot, write some tests!"
    if INPUT_TYPE:
        main(os.path.join('io', '{}_{}.in'.format(PROB_NAME, INPUT_TYPE)),
             os.path.join('io', '{}_{}.out'.format(PROB_NAME, INPUT_TYPE)))
    unittest.main()
