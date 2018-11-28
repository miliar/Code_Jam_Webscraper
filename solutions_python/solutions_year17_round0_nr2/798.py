import sys
import os
import math

from tqdm import tqdm

# fin = open('test.in')
fin = open('B-large.in.txt')
# fout = sys.stdout
fout = open('out_1_large', 'w')

def ok(st):
    keep = 0
    for sym in st:
        if intize(sym) < keep:
            return False
        keep = intize(sym)
    return True

def intize(s):
    return int(s + '0') / 10

def solve(n):
    ns = str(n)

    candidates = []
    if ok(ns):
        candidates.append(n)

    for preflen in range(len(ns) + 1):
        for suflen in range(len(ns) + 1):
            pref = str(max(intize(ns[:preflen]) - 1, 0))
            suf = '9' * suflen

            # print '--> %s is %s' % (pref, ok(pref))
            if ok(pref):
                num = intize(pref + suf)
                if num <= n:
                    candidates.append(num)

    return max(candidates)



if __name__ == '__main__':
    count = int(fin.readline().strip())

    for i in range(count):
        n = int(fin.readline().strip())
        result = solve(n)
        fout.write('Case #%s: %s\n' % (i + 1, result))


