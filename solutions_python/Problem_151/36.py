#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Uses https://github.com/rkistner/contest-algorithms

import sys


def perm(N, i):
    if i == 0:
        return [[]]
    result = []
    for j in range(N):
        for p in perm(N, i-1):
            result.append(p + [j])
    return result

def debug(*args):
    print(*args, file=sys.stderr)

def count(words):
    trie = {}
    for word in words:
        for i in range(0, len(word)+1):
            prefix = word[:i]
            trie[prefix] = 1
    return len(trie)

fin = sys.stdin
T = int(fin.readline())
for case in range(1, T + 1):
    M, N = map(int, fin.readline().split())
    words = []
    for i in range(M):
        words.append(fin.readline().strip())

    worst = 0
    counter = {}

    for permutation in perm(N, M):
        groups = []
        for i in range(N):
            groups.append([])
        for i, word in enumerate(words):
            groups[permutation[i]].append(word)
        c = 0
        for group in groups:
            c += count(group)
        if c not in counter:
            counter[c] = 0
        counter[c] += 1
        worst = max(worst, c)


    print("Case #%d: %d %d" % (case, worst, counter[worst]))