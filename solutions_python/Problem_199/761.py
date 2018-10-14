import sys
import os
import math

# fin = open('test.in')
fin = open('A-large.in.txt')
# fout = sys.stdout
fout = open('out_1_large', 'w')

def flip(s, k, i):
    for j in range(i, i + k):
        s[j] = not s[j]

def solve(s, k):
    flips = 0
    for i in range(len(s) - k + 1):
        if not s[i]:
            flip(s, k, i)
            flips += 1
    return flips if all(s[len(s) - k:]) else 'IMPOSSIBLE'

if __name__ == '__main__':
    count = int(fin.readline().strip())

    for i in range(count):
        s, k = fin.readline().strip().split()
        result = solve([x == '+' for x in s], k = int(k))
        fout.write('Case #%s: %s\n' % (i + 1, result))


