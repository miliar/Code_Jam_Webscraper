from math import pi
from collections import namedtuple

Pancake = namedtuple('Pancake', 'R H')
Test = namedtuple('Test', 'N K cakes')

def read(lines):
    while lines:
        N, K = map(int, lines.pop(0).split())
        cakes = (Pancake(*map(int, line.split())) for line in lines[:N])
        cakes = tuple(sorted(cakes, key=lambda c: (c.R, c.H), reverse=True))
        yield Test(N, K, cakes)
        del lines[:N]

def solve(test):
    def area(cakes):
        radii = max([c.R for c in cakes], default=0)
        return pi * radii ** 2 + sum(c.H * pi * c.R * 2 for c in cakes)

    combs = {0: []}
    for c in test.cakes:
        news = {cmb + 1: combs[cmb] + [c] for cmb in combs if cmb < test.K}
        for n in news:
            combs[n] = max(combs.get(n, []), news[n], key=area)

    return area(combs[max(combs)])


if __name__ == '__main__':
    infile = 'A-small-attempt0.in'

    with open(infile) as src:
        lines = list(src.readlines())

    number = int(lines[0])
    tests = list(read(lines[1:]))

    with open(infile.replace('.in', '.out'), 'w') as dst:
        for i, test in enumerate(tests, 1):
            dst.write('Case #{}: {}\n'.format(i, solve(test)))
