import numpy as np
from collections import Counter

def parse(input_file, output_file):
    with open(input_file) as f:
        T = int(f.readline().split()[0])
        out = open(output_file, 'w')
        for i in range(T):
            l = list(map(int, f.readline().split()))
            #D, N = map(int, f.readline().split())
            #rows = []
            #for _ in range(N):
            #    rows.append(list(map(int, f.readline().split())))
            sol = solve(l)
            line = "Case #"+str(i+1)+": "+str(sol)
            print(line)
            check(l, sol, i+1)
            out.write(line+'\n')
    return


def solve_small(l):
    N, R, O, Y, G, B, V = l
    assert O == 0 and G == 0 and V == 0
    # R Y B
    if R>Y+B or Y>R+B or B>Y+R:
        return 'IMPOSSIBLE'
    cs = [(B, 'B'), (Y, 'Y'), (R, 'R')]
    cs.sort(reverse=True)
    (c1n, c1), (c2n, c2), (c3n, c3) = cs
    res = [c1, c2]*c2n
    res += [c1, c3]*(c1n-c2n)
    pos_in_res = 0
    for _ in range(c3n+c2n-c1n):
        res[pos_in_res] += c3
        pos_in_res += 1

    return ''.join(res)

def anti_color(c):
    if c in 'RG':
        return 'RG'.replace(c, '')
    if c in 'YV':
        return 'YV'.replace(c, '')
    if c in 'BO':
        return 'BO'.replace(c, '')

def decomp_color(c):
    if c in 'RYB':
        return c
    if c == 'G':
        return 'YB'
    if c == 'V':
        return 'RB'
    if c == 'O':
        return 'RY'

def can_next(c1, c2):
    s = set.intersection(set(decomp_color(c1)), set(decomp_color(c2)))
    return not len(s)

def check(l, res, n):
    if res == 'IMPOSSIBLE':
        print('############## imp {}'.format(n))
        return
    N, R, O, Y, G, B, V = l
    count = dict(zip(['R', 'O', 'Y', 'G', 'B', 'V'], [R, O, Y, G, B, V]))
    res_count = Counter(res)
    assert len(res) == N
    for c in count:
        assert count[c] == res_count[c]

    for a, b in zip(res[:-1], res[1:]):
        assert can_next(a, b)
    assert can_next(res[-1], res[0])


def solve(l):
    N, R, O, Y, G, B, V = l
    if O == 0 and G == 0 and V == 0:
        return solve_small(l)

    new_l = [N, R-G, 0, Y-V, 0, B-O, 0]
    if min(new_l) < 0:
        return 'IMPOSSIBLE'
    res = solve_small(new_l)
    if res == 'IMPOSSIBLE':
        return 'IMPOSSIBLE'

    count = dict(zip(['R', 'O', 'Y', 'G', 'B', 'V'], [R, O, Y, G, B, V]))
    to_do = {'G':G, 'V':V, 'O':O}
    for comp_c in to_do:
        anti_c = anti_color(comp_c)
        if to_do[comp_c] > 0:
            if count[anti_c] > count[comp_c]:
                res = res.replace(anti_c, anti_c+(comp_c+anti_c)*to_do[comp_c])
                to_do[comp_c] = 0

    left_to_do = 0
    for comp_c in to_do:
        if to_do[comp_c] > 0:
            left_to_do += 1
    if left_to_do == 0:
        return res
    if left_to_do >= 2:
        return 'IMPOSSIBLE'
    if left_to_do == 1:
        if len(res):
            return 'IMPOSSIBLE'
        for comp_c in to_do:
            if to_do[comp_c] > 0:
                anti_c = anti_color(comp_c)
                res = (comp_c+anti_c)*to_do[comp_c]
                return res
    assert False




dir = "./"

input_file = dir+"B-test.in"
output_file = dir+"B-test.txt"

input_file = dir+"B-small-attempt0.in"
output_file = dir+"B-small-attempt0.out"
'''

input_file = dir+"B-large.in"
output_file = dir+"B-large.out"
'''
parse(input_file, output_file)


