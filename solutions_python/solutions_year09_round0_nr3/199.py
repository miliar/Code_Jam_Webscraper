#!/usr/bin/env python

import sys
import string

def main():
    f = open(sys.argv[1])
    lines = f.readlines()
    f.close()

    N = int(lines[0].strip())
    for case in range(N):
        print "Case #%d: %04d" % (case+1, solve(lines[1+case].strip()))

def solve(s):
    wtcj = 'welcome to code jam'

    indices = []
    for i in range(len(wtcj)):
        indices.append([])
        for j in range(len(s)):
            if s[j] == wtcj[i]:
                indices[i].append(j)

    matches = [[-1]]
    for iset in indices:
        new_matches = []
        for i in iset:
            for match in matches:
                if match[-1] < i:
                    new_matches.append(match + [i])
        matches = new_matches

    return len(matches) % 10000

if __name__ == '__main__':
    main()