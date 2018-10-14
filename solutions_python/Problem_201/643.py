import sys
import multiprocessing
from collections import defaultdict


def parse(input_file):
    """Returns a iterable that elements are single test cases."""
    t = int(input_file.readline())
    for _ in range(t):
        n, k = map(int, input_file.readline().split())
        yield n, k


def solve(n, k):
    """Main code."""
    spans = defaultdict(int)
    spans[n] = 1
    while True:
        length = max(spans)
        count = spans.pop(length)
        l, r = length // 2, (length - 1) // 2
        if count >= k:
            return "{} {}".format(l, r)
        else:
            k -= count
            spans[l] += count
            spans[r] += count


def tee(line, file):
    if file != sys.stdout:
        print(line)
    print(line, file=file)


def save(answers, output_file):
    for i, answer in enumerate(answers):
        tee("Case #{case_num}: {answer}".format(case_num=i+1, answer=answer), file=output_file)


def do_solve(case):
    return solve(*case)


def solve_all(input_file, output_file):
    pool = multiprocessing.Pool()
    answers = pool.map(do_solve, parse(input_file))
    pool.close()
    save(answers, output_file)


def main():
    if len(sys.argv) == 1:
        solve_all(sys.stdin, sys.stdout)
    else:
        input_file_name = sys.argv[1]
        output_file_name = input_file_name.replace(".in", ".out")
        with open(input_file_name) as input_file, open(output_file_name, "w") as output_file:
            solve_all(input_file, output_file)


if __name__ == '__main__':
    main()