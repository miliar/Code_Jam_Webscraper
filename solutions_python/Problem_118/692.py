#!/usr/bin/env python3
from itertools import chain
import sys

PROBLEM_LETTER = 'C'
DIFFICULTY = sys.argv[1]
INPUT_FILE = '{0}-{1}.in'.format(PROBLEM_LETTER, DIFFICULTY)
OUTPUT_FILE = '{0}-{1}.out'.format(PROBLEM_LETTER, DIFFICULTY)

good = {1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121,
        123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004,
        1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121,
        1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004}


def solve(fin):
    A, B = tuple(int(s) for s in fin.readline().split())
    return len([n for n in good if A <= n <= B])

if __name__ == "__main__":
    fin = open(INPUT_FILE, 'r')
    fout = open(OUTPUT_FILE, 'w')

    testCount = int(fin.readline())
    for i in range(testCount):
        answer = solve(fin)
        fout.write('Case #{0}: {1}\n'.format(i + 1, answer))

    fin.close()
    fout.close()
