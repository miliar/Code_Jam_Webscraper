#!/usr/bin/env python2.6
import re

def matcher(pattern):
    i = 0
    regex = ''
    while i < len(pattern):
        if pattern[i] == '(':
            i += 1
            regex += '('
            while pattern[i+1] != ')':
                regex += pattern[i] + '|'
                i += 1
            regex += pattern[i]
            i += 1
        else:
            regex += pattern[i]
            i += 1
    return '^%s$' % regex

def main():
    with open('A-large.in') as f:
        L, D, N = map(int, f.readline().split())
        words = []
        for i in range(D):
            words.append(f.readline().rstrip())
        cases = []
        for i in range(N):
            cases.append(f.readline().rstrip())
        compiled = [re.compile(matcher(case)) for case in cases]
        kth = 1
        for case in compiled:
            matches = 0
            for word in words:
                if case.search(word):
                    matches += 1
            print 'Case #%d: %d' % (kth, matches)
            kth += 1

if __name__ == '__main__':
    main()
