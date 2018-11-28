import sys
import numpy as np
import itertools

def sol(s):
    s = sorted(s)
    counts = dict()
    res = ''

    for l in range(28):
        counts[chr(l + ord('A'))] = 0
    for l in s:
        counts[l] = counts.get(l, 0) + 1

    res = res + '0'*counts['Z']
    counts['E'] -= counts['Z']
    counts['R'] -= counts['Z']
    counts['O'] -= counts['Z']
    counts['Z'] -= counts['Z']

    res = res + '2'*counts['W']
    counts['T'] -= counts['W']
    counts['O'] -= counts['W']
    counts['W'] -= counts['W']

    res = res + '6'*counts['X']
    counts['S'] -= counts['X']
    counts['I'] -= counts['X']
    counts['X'] -= counts['X']

    res = res + '7'*counts['S']
    counts['E'] -= counts['S']
    counts['V'] -= counts['S']
    counts['E'] -= counts['S']
    counts['N'] -= counts['S']
    counts['S'] -= counts['S']

    res = res + '8'*counts['G']
    counts['E'] -= counts['G']
    counts['I'] -= counts['G']
    counts['H'] -= counts['G']
    counts['T'] -= counts['G']
    counts['G'] -= counts['G']

    res = res + '3'*counts['T']
    counts['H'] -= counts['T']
    counts['R'] -= counts['T']
    counts['E'] -= 2 * counts['T']
    counts['T'] -= counts['T']

    res = res + '4'*counts['R']
    counts['F'] -= counts['R']
    counts['O'] -= counts['R']
    counts['U'] -= counts['R']
    counts['R'] -= counts['R']

    res = res + '1'*counts['O']
    counts['N'] -= counts['O']
    counts['E'] -= counts['O']
    counts['O'] -= counts['O']

    res = res + '5'*counts['F']
    counts['I'] -= counts['F']
    counts['V'] -= counts['F']
    counts['E'] -= counts['F']
    counts['F'] -= counts['F']
    res = res + '9'*(counts['N']/2)

    return ''.join(map(str, sorted(res)))

inp = open(sys.argv[1])
out = open(sys.argv[2], 'w')
T = int(inp.readline())
for i in range(T):
    s = inp.readline()
    out.write("Case #{}: {}\n".format(i+1, sol(s)))
inp.close()
out.close()