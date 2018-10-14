import math


INPUT_FILE = __file__.replace('.py', '.input')
OUTPUT_FILE = __file__.replace('.py', '.output')


def farea(r):
    return math.pi*r**2


def sarea(r, h):
    return 2*math.pi*r*h


def uparea(r, h):
    return farea(r) + sarea(r, h)


def total(pancakes):
    max_r = max(pancake[0] for pancake in pancakes)
    return farea(max_r) + sum(sarea(r, h) for r, h in pancakes)


def solve(pancakes, k):
    sides = sorted(pancakes, key=lambda p: sarea(*p), reverse=True)
    bottoms = sorted(pancakes, key=lambda p: uparea(*p), reverse=True)
    if bottoms[0] in sides[:k]:
        return total(sides[:k])
    else:
        km1sides = sides[:k-1]
        if km1sides:
            min_r = min(p[0] for p in km1sides)
            bottoms = [p for p in bottoms if p[0] >= min_r]
        return total([bottoms[0]] + km1sides)


def main():

    with open(INPUT_FILE, 'r') as f, open(OUTPUT_FILE, 'w') as h:
        t = int(f.readline().strip())
        for i in xrange(1, t+1):
            n, k = map(int, f.readline().strip().split())
            pancakes = []
            for __ in xrange(n):
                pancakes.append(tuple(map(int, f.readline().strip().split())))
            soln = solve(pancakes, k)
            outline = 'Case #{i}: {soln:.9f}\n'.format(**locals())
            h.write(outline)
            print outline,


if __name__ == '__main__':
    main()
