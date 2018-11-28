import math

import itertools


class Pancake(object):
    def __init__(self, line):
        self.r, self.h = map(float, line.split())
        sides = math.pi * 2 * self.r * self.h
        self.contribution_bottom = math.pi*self.r**2 + sides
        self.contribution_middle = sides

    def __repr__(self): return '<{0.r!r} {0.h!r}>'.format(self)

def solve(k, pancake_lines):
    n = len(pancake_lines)
    pancakes = list(map(Pancake, pancake_lines))
    pancakes.sort(key=lambda x: x.contribution_middle, reverse=True)
    best = 0.
    for i, bottom_pancake in enumerate(pancakes):
        score = bottom_pancake.contribution_bottom
        extra_pancakes = list(itertools.islice(filter(lambda p: p.r <= bottom_pancake.r and p is not bottom_pancake,
                                                      pancakes), k - 1))
        #print((i, bottom_pancake, len(extra_pancakes), k-1, extra_pancakes))
        if len(extra_pancakes) != k - 1:
            continue
        score += sum(p.contribution_middle for p in extra_pancakes)
        best = max(best, score)
    return best





if __name__ == '__main__':
    import io
    lines = list(io.open('A-large.in', 'r').readlines())
    i = 1
    x = 1
    while i < len(lines):
        n, k = lines[i].split()
        n = int(n)
        k = int(k)
        pancake_lines = lines[i + 1:i + n + 1]
        i += n+1
        print('Case #{}: {:.6f}'.format(x, solve(k, pancake_lines)))
        x += 1