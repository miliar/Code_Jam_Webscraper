#! /usr/bin/env python


def main():
    with open('a.in', 'r') as fin, open('a.out', 'w') as fout:
        num_cases = int(fin.readline())
        for case in range(1, num_cases + 1):
            cakes, k = fin.readline().split()
            pancakes = [cake == '+' for cake in cakes]
            answer = solve(pancakes, int(k))
            fout.write('Case #{0}: {1}\n'.format(case, answer))


def solve(cakes, k):
    flips = 0
    for i in range(len(cakes) - k + 1):
        if not cakes[i]:
            flips += 1
            for j in range(k):
                cakes[i+j] = not cakes[i+j]
    if set(cakes) == set([True]):
        return flips
    else:
        return 'IMPOSSIBLE'


if __name__ == '__main__':
    main()
