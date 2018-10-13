# coding: utf8
# Copyright: MathDecision

import math

def solve(n, k, pancakes):
    pancakes = sorted(pancakes, key=lambda x: -(x[0] * x[1]))
    round1 = pancakes[:k]
    round1 = sorted(round1, key=lambda x: -x[0])
    # print round1
    if n > k:
        round2 = pancakes[k:]
        r0, h0 = round1[0]
        r, h = max(round2, key = lambda x: x[0]**2 + 2 * x[0] * x[1])
        if r**2 + 2 * r * h > r0**2 + 2 * r0 * h0:
            round1[0] = (r, h)
    r0, h0 = round1[0]
    return (sum([2 * r * h for r, h in round1]) + r0**2) * math.pi

def solve2(n, k, pancakes):
    pancakes = sorted(pancakes, key=lambda x: - (x[0]**2 + 2 * x[0] * x[1]))
    base = pancakes[0]
    if k > 1:
        pancakes = sorted(pancakes[1:], key=lambda x: -(x[0] * x[1]))
        select = [base] + pancakes[:k - 1]
    else:
        select = [base]
    return (sum([2 * r * h for r, h in select]) + select[0][0]**2) * math.pi

def solve3(n, k, pancakes):
    pancakes = sorted(pancakes, key=lambda x: - (x[0] * x[1]))
    base = pancakes[0]
    if k > 1:
        pancakes = sorted(pancakes[1:], key=lambda x: -(x[0] * x[1]))
        select = [base] + pancakes[:k - 1]
    else:
        select = [base]
    return (sum([2 * r * h for r, h in select]) + select[0][0]**2) * math.pi

if __name__ == '__main__':
    file_number = 7
    problem_name = 'amplesyrup'
    infile = '{}{}.in'.format(problem_name, file_number)
    outfile = '{}{}.out'.format(problem_name, file_number)
    responses = []
    with open(infile, 'r') as f:
        cases = int(f.readline())
        for _ in range(cases):
            n, k = map(lambda x: int(x), f.readline().split(' '))
            pancakes = []
            for i in range(n):
                r, h = map(lambda x: float(x), f.readline().split(' '))
                pancakes.append((r, h))
            # print D, N, horses
            # print sol(horses, D)
            responses.append(max(solve(n, k, pancakes), solve2(n, k, pancakes), solve3(n, k, pancakes)))

    with open(outfile, 'w') as f:
        for i, r in enumerate(responses):
            f.write('Case #{}: {:.7f}\n'.format(i + 1, r))
