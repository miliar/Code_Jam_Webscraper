from collections import namedtuple

Test = namedtuple('Test', 'N K')

def read(line):
    return Test(*[int(c) for c in line.split()])

def split(n):
    return [(n - 1) // 2, (n - 1) // 2 + (n % 2 == 0)]

def solve(test):
    if test.N == test.K:
        return '0 0'

    blobs = [test.N]
    for k in range(test.K - 1):
        large = blobs.pop(0)
        blobs.extend([b for b in split(large) if b])
        blobs.sort(reverse=True)

    return ' '.join(map(str, (sorted(split(blobs[0]), reverse=True))))

if __name__ == '__main__':
    infile = 'C-small-1-attempt0.in'

    with open(infile) as src:
        lines = list(src.readlines())

    number = int(lines[0])
    tests = [read(line) for line in lines[1:]]

    with open(infile.replace('.in', '.out'), 'w') as dst:
        for i, test in enumerate(tests, 1):
            dst.write('Case #{}: {}\n'.format(i, solve(test)))
