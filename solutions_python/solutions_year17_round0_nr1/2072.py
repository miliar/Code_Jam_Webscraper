from collections import namedtuple

Test = namedtuple('Test', 'cakes length')

def read(line):
    cakes, length = line.split()
    return Test(tuple([c == '+' for c in cakes]), int(length))

def solve(test):
    flipper = [True] * test.length
    cakes = list(test.cakes)

    count = 0
    for i in range(len(cakes) - test.length + 1):
        if not cakes[i]:
            flipped = [not c for c in cakes[i:i+test.length]]
            cakes[i:i+test.length] = flipped
            count += 1

    return count if all(cakes) else 'IMPOSSIBLE'

if __name__ == '__main__':
    infile = 'A-large.in'

    with open(infile) as src:
        lines = list(src.readlines())

    number = int(lines[0])
    tests = [read(line) for line in lines[1:]]

    with open(infile.replace('.in', '.out'), 'w') as dst:
        for i, test in enumerate(tests, 1):
            dst.write('Case #{}: {}\n'.format(i, solve(test)))
