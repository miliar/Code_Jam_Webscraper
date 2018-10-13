import os
import sys


def process_file(in_name, out_name):
    with open(in_name, 'r') as fin:
        with open(out_name, 'w') as fout:
            def read():
                while - True:
                    l = fin.readline()
                    if len(l) == 0:
                        raise Exception('EOF')
                    l = l.strip('\n')
                    if len(l):
                        return l

            def write(*args):
                fout.write(' '.join(map(str, args)))

            t = int(fin.readline())
            for i in range(t):
                print(f'Case #{i + 1}: ')
                write(f'Case #{i + 1}: ')
                solve(read, write)


def solve(read, write):
    N, R, O, Y, G, B, V = map(int, read().split())
    r = ans(N, R, O, Y, G, B, V)
    print(N, R, O, Y, G, B, V, ' => ', r)
    if r not in ['IMPOSSIBLE', 'UNKNOWN']:
        print(valids(r))
        assert (valids(r))

    write(f'{r}\n')


def ans(N, R, O, Y, G, B, V):
    if O or G or V:
        return 'UNKNOWN'
    assert O == 0
    assert G == 0
    assert V == 0
    counts = [(R, 'R'), (B, 'B'), (Y, 'Y')]
    counts.sort(reverse=True)
    c1 = list(counts[0])
    c2 = list(counts[1])
    c3 = list(counts[2])
    s1 = c1[1] * c1[0]
    diff = c2[0] - c3[0]
    s2 = c2[1] * diff + (c3[1] + c2[1]) * c3[0]
    s = ''
    i = 0
    j = 0
    while i < len(s1) or j < len(s2):
        while i < len(s1) and j < len(s2):
            s += s1[i]
            s += s2[j]
            i += 1
            j += 1
        if i < len(s1):
            return 'IMPOSSIBLE'
        while j < len(s2):
            s += s2[j]
            j += 1
    assert valids(s)
    return s


#
# def permutation(list):
#     n = len(list)
#     if n < 2:
#         yield list
#     else:
#         for perm in permutation(list[1:]):
#             for i in range(len(perm) + 1):
#                 yield perm[:i] + [list[0]] + perm[i:]
#
#
def valid2s(x, y):
    if x == 'R':
        return y != 'V' and y != 'O' and y != 'R'
    if x == 'B':
        return y != 'V' and y != 'G' and y != 'B'
    if x == 'Y':
        return y != 'G' and y != 'O' and y != 'Y'
    if x == 'V':
        return y == 'Y'
    if x == 'O':
        return y == 'B'
    if x == 'G':
        return y == 'R'


def valids(s):
    n = len(s)
    for i in range(n):
        if not valid2s(s[i], s[(i - 1) % n]):
            return False
        if not valid2s(s[i], s[(i + 1) % n]):
            return False
    return True


# def valid2(x, y):
#     if x == R:
#         return y != RB and y != RY and y != R
#     if x == B:
#         return y != RB and y != BY and y != B
#     if x == Y:
#         return y != BY and y != RY and y != Y
#     if x == RB:
#         return y == Y
#     if x == RY:
#         return y == B
#     if x == BY:
#         return y == R
#
#
# def valid(list):
#     n = len(list)
#     for i in range(n):
#         if not valid2(list[i], list[(i - 1) % n]):
#             return False
#         if not valid2(list[i], list[(i + 1) % n]):
#             return False
#     return True

#
#
# R = 1
# B = 2
# Y = 3
# RB = 4
# RY = 5
# BY = 6
#
# l = [1, 2, 1, 2, 3, 3, 3, 3]
# for p in permutation(l):
#     if valid(p):
#         print(p, valid(p))


if __name__ == '__main__':
    args = sys.argv
    if len(args) >= 2:
        in_name = args[1]
        out_name = args[2] if len(args) == 3 else (
            (in_name[:-3] if in_name.endswith('.in')
             else in_name) + '.out')
        process_file(in_name, out_name)
    else:
        for in_name in os.listdir():
            if in_name.endswith('.in'):
                out_name = in_name[:-3] + '.out'
                process_file(in_name, out_name)
