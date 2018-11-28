from sys import argv
from math import ceil, floor

def readInput(fl):
    inputs = [ln for n, ln in enumerate(open(fl).readlines()) if n % 2 == 0 and n != 0]
    return inputs

def solve1(n_case, ln):
    pancakes = [float(p) for p in ln.split()]
    pancakes.sort(reverse=True)
    minimum = max(pancakes)
    bound = False
    special_min = 0
    while not bound:
        special_min += 1
        if pancakes[0] == 9.0:
            pancakes[0] = 6.0
            pancakes.append(3.0)
        else:
            pancakes.append(floor(pancakes[0]/2))
            pancakes[0] = ceil(pancakes[0]/2)
        pancakes.sort(reverse=True)
        if special_min + pancakes[0] < minimum:
            minimum = special_min + pancakes[0]
        if pancakes[0] < 4:
            bound = True
    return minimum

def solve2(n_case, ln):
    pancakes = [float(p) for p in ln.split()]
    pancakes.sort(reverse=True)
    minimum = max(pancakes)
    bound = False
    special_min = 0
    while not bound:
        special_min += 1
        pancakes.append(floor(pancakes[0]/2))
        pancakes[0] = ceil(pancakes[0]/2)
        pancakes.sort(reverse=True)
        if special_min + pancakes[0] < minimum:
            minimum = special_min + pancakes[0]
        if pancakes[0] < 4:
            bound = True
    return minimum

def solve(n_case, ln):
    print 'Case #%d: %d' % (n_case + 1, int(min(solve1(n_case, ln), solve2(n_case, ln))))

if __name__ == '__main__':
    inputs = readInput(argv[1])
    for n_case, ln in enumerate(inputs):
        solve(n_case, ln)
