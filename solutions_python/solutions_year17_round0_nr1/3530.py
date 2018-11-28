#!/usr/bin/env python
import sys
import ipdb

def calc(ifile):
    S, K = ifile.readline().split(' ')
    S = list(S)
    K = int(K.strip())

    num_flips = 0
    # iterate over S
    for i, _ in enumerate(S):
        if S[i] == '-':
            num_flips += 1
            for j in range(K):
                try:
                    S[i+j] = '+' if S[i+j] == '-' else '-'
                except IndexError:
                    return 'IMPOSSIBLE'
    if '-' in S:
        return 'IMPOSSIBLE'
    else:
        return str(num_flips)




if __name__ == "__main__":
    if len(sys.argv) > 1:
        ifile = open(sys.argv[1])
    else:
        ifile = sys.stdin
    if len(sys.argv) > 2:
        ofile = open(sys.argv[2], 'w')
    else:
        ofile = sys.stdout
    for i in range(int(ifile.readline())):
        ofile.write("Case #%i: %s\n" % (i+1, calc(ifile)))
