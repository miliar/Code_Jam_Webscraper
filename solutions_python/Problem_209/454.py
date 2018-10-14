__author__ = 'paolo'
from math import pi
import decimal


class Pancake:
    def __init__(self, f):
        self.radius, self.height = [int(x) for x in f.readline().split()]

    def areah(self):
        return 2 * decimal.Decimal(pi) * decimal.Decimal(self.radius) * decimal.Decimal(self.height)

    def areat(self):
        return decimal.Decimal(pi) * decimal.Decimal(self.radius) * decimal.Decimal(self.radius)


class Problem:
    def __init__(self, f):
        self.n, self.k = [int(x) for x in f.readline().split()]
        self.pancakes = []
        for _ in range(self.n):
            self.pancakes.append(Pancake(f))

    def solve(self):
        hsorted = sorted(self.pancakes, key=Pancake.areah, reverse=True)
        tsorted = sorted(self.pancakes, key=Pancake.areat)
        maxarea = decimal.Decimal(0.0)
        for t in tsorted:
            totarea = t.areat() + t.areah()
            added = 1
            for h in hsorted:
                if added >= self.k:
                    break
                if t != h and t.radius >= h.radius:
                    totarea += h.areah()
                    added += 1
            if totarea > maxarea:
                maxarea = totarea
        return maxarea

with open('a.in', 'r') as infile:
    nproblems = int(infile.readline())
    problems = []
    for _ in range(nproblems):
        problems.append(Problem(infile))

with open('a.out', 'w') as outfile:
    for i in range(nproblems):
        outfile.write('Case #{}: {}\n'.format(i + 1, problems[i].solve()))
