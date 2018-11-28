import sys
import os


def problem_specific_parser(src):
    line = next(src)
    max_shyness, audience = line.split(' ')
    return int(max_shyness), [int(e) for e in audience]


def solve(data):
    max_shyness, audience = data
    nstanding = 0
    nfriends = 0

    for shyness, a in enumerate(audience[:max_shyness + 1]):
        missing = max([shyness - nstanding, 0])
        nfriends += missing
        nstanding += missing + a

    return nfriends


def parse(src):
    lines = iter(src.split(os.linesep))
    nproblems = int(next(lines))

    for problem in range(nproblems):
        yield problem_specific_parser(lines)


def main():
    src = sys.stdin.read()
    for i, data in enumerate(parse(src)):
        print("Case #{0}: {1}".format(i + 1, solve(data)))

    
if __name__ == '__main__':
    main()
