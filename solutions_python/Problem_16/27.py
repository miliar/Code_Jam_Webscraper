#!/usr/bin/python2.5
# Solution to Google Code Jam 08 Round 2 Problem D
# Matt Giuca

# Usage: ./probD.py < inputfile > outputfile

import sys
import copy

DEBUG = False

def parse(file=sys.stdin):
    """
    (Generator) Read input file from filename or file or stdin,
    return a structure.
    Yields (k, S)
    """
    if isinstance(file, basestring):
        file = open(file)
        toclose = True
    else:
        toclose = False
    n = int(file.readline().strip())
    for i in range(n):
        # build array of nodes
        nodes = []
        k = int(file.readline().strip())
        S = file.readline().strip()
        yield k, S
    if toclose:
        file.close()

def gen_all_perms_ints(k):
    return gen_all_perms(range(1,k+1))

def gen_all_perms(l):
    """
    Yields all permutations of list.
    """
    if len(l) == 1:
        yield l
    for i in range(len(l)):
        item = l[i]
        rest = l[:i] + l[i+1:]
        for sub_perm in gen_all_perms(rest):
            yield [item] + sub_perm

def solve_case(k, S):
    # BRUTE FORCE!
    best = None
    for perm in gen_all_perms_ints(k):
        this = compression(apply_perm(perm, S))
        if best is None or this < best:
            best = this
    return best

def apply_perm(perm, S):
    """
    Apply permutation perm (list of ints) to string S.
    """
    k = len(perm)
    chunks = []
    for i in range(0, len(S), k):
        s = S[i:i+k]
        s = ''.join(s[perm[j]-1] for j in range(k))
        chunks.append(s)
    return ''.join(chunks)

def compression(S):
    """
    Compute the compressed size of string S.
    """
    if len(S) == 0:
        return 0
    cur = S[0]
    size = 1
    for c in S[1:]:
        if c != cur:
            cur = c
            size += 1
    return size

def main(file=sys.stdin):
    """
    Processes input, prints output to stdout.
    """
    i = 0
    for k, S in parse(file):
        i += 1
        answer = solve_case(k, S)
        print("Case #%d: %d" % (i, answer))

if __name__ == "__main__":
    main()
