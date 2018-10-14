import os
import time
import pytest
import collections
from contextlib import contextmanager
from typing import List


INPUT_TYPE = 'large'


Case = collections.namedtuple('Case', ['n'])


def solve(case: Case):
    """break 'case', solve and return the solution"""

    digits = [int(digit) for digit in str(case.n)]
    last = 9
    for i in range(len(digits))[::-1]:
        current = digits[i]
        if current > last:
            for j in range(len(digits))[::-1]:
                if j == i:
                    break
                digits[j] = 9
            digits[i] -= 1
        last = digits[i]
    return int(''.join(str(d) for d in digits))


def read_case(lines: List[str]) -> Case:
    """Read a test case from the input."""
    n = int(lines.pop(0))
    return Case(n)


def read_file(filepath: str) -> List[Case]:
    """Read the input `filepath` and return a list of cases."""
    cases = []
    with open(filepath, 'rt') as fobj:
        lines = fobj.readlines()
        num_cases = int(lines.pop(0))
        for _ in range(num_cases):
            cases.append(read_case(lines))
    return cases


def write_results(results: List, outfile: str) -> None:
    with open(outfile, 'wt') as f:
        for idx, result in enumerate(results):
            f.write('Case #{}: {}\n'.format(idx + 1, result))


@contextmanager
def timing(prefix):
    start = time.time()
    yield
    print('{} took {} seconds.'.format(prefix, time.time() - start))


def main(infile: str, outfile: str) -> None:
    cases = read_file(infile)
    results = []
    for idx, case in enumerate(cases):
        with timing("Solving case #{}".format(idx + 1)):
            results.append(solve(case))
    write_results(results, outfile)


test_cases = {
    Case(132): 129,
    Case(1000): 999,
    Case(111111111111111110): 99999999999999999,
}


@pytest.mark.parametrize(('case', 'result'), test_cases.items())
def test_function(case: Case, result):
    assert solve(case) == result


if __name__ == '__main__':
    pytest.main(args=[__file__])
    if INPUT_TYPE:
        main(os.path.join('io', '{}.in'.format(INPUT_TYPE)),
             os.path.join('io', '{}.out'.format(INPUT_TYPE)))
