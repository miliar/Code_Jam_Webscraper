import os

PROB_NAME = 'fair_and_square'
INPUT_TYPE = 'large1'

fss = []
with open(r'io\fs', 'rt') as f:
    for line in f:
        fss.append(int(line))


def palindrome(num):
    return num == int(''.join(reversed(str(num))))


def find_palindromes(limit):
    num = 1
    with open(r'io\palindromes', 'wt') as f:
        while num < limit:
            if palindrome(num):
                f.write('{}\n'.format(num))
                print num
            num += 1


def find_fair_and_square(ps):
    with open(r'io\fs', 'wt') as f:
        for p in ps:
            r = p ** 2
            if palindrome(r):
                f.write('{}\n'.format(r))
                print r


def solve(case):
    """break 'case', solve and return the solution"""
    a, b = case
    return sum(1 for num in fss if num >= a and num <= b)


def read_file(filepath):
    """Read the input file and return a list of cases in a tuple format."""
    cases = []
    with open(filepath, 'rt') as fobj:
        lines = fobj.readlines()
        num_cases = int(lines.pop(0))
        for case in range(num_cases):
            cases.append(tuple(int(num) for num in lines.pop(0).split()))
    return cases


def write_results(results, outfile):
    with open(outfile, 'wt') as f:
        for idx, result in enumerate(results):
            f.write('Case #{}: {}\n'.format(idx + 1, result))


def main(infile, outfile):
    cases = read_file(infile)
    results = [solve(case) for case in cases]
    write_results(results, outfile)

main(os.path.join('io', '{}_{}.in'.format(PROB_NAME, INPUT_TYPE)),
     os.path.join('io', '{}_{}.out'.format(PROB_NAME, INPUT_TYPE)))

# find_palindromes(10 ** 7 + 1)

# ps = []
# with open(r'io\palindromes', 'rt') as f:
#    for line in f:
#        ps.append(int(line))
# find_fair_and_square(ps)
