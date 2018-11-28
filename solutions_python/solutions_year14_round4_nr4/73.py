#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys
import os

def build_trie(words):
    if not words:
        return -999999
    prefixes = set()
    for w in words:
        for i in xrange(1, len(w)):
            prefixes.add(w[:i])
        prefixes.add(w)
    return len(prefixes) + 1

def main():
    T = int(sys.stdin.readline())
    for _t in xrange(1, T+1):
        M, N = map(int, sys.stdin.readline().split())
        words = []
        best = -1
        cnt = 0
        for _ in xrange(M):
            w = sys.stdin.readline().strip()
            words.append(w)
        for i in xrange(N ** M):
            servers = [list() for x in xrange(N)]
            t = i
            for w in words:
                servers[t % N].append(w)
                t /= N
            total = sum([build_trie(s) for s in servers])
            if total > best:
                best = total
                cnt = 1
            elif total == best:
                cnt += 1
        print "Case #" + str(_t) + ":", best, cnt


if __name__ == '__main__':
    main()
