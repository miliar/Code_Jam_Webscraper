from collections import namedtuple

Test = namedtuple('Test', 'D N horses')

def read(lines):
    while lines:
        D, N = map(int, lines.pop(0).split())
        horses = tuple(tuple(map(int, line.split())) for line in lines[:N])
        yield Test(D, N, horses)
        del lines[:N]

def solve(test):
    return test.D / max((test.D - h[0]) / h[1] for h in test.horses)

if __name__ == '__main__':
    infile = 'A-large.in'

    with open(infile) as src:
        lines = list(src.readlines())

    number = int(lines[0])
    tests = list(read(lines[1:]))

    with open(infile.replace('.in', '.out'), 'w') as dst:
        for i, test in enumerate(tests, 1):
            dst.write('Case #{}: {}\n'.format(i, solve(test)))
