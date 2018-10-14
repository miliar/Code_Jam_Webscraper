#!/usr/bin/env python

"""Google Code Jam, Online Round 1."""

import sys

def useage():
    """Prints useage instructions."""
    print "useage: " + sys.argv[0] + " FILE"
    print "where FILE is the path and name of a valid input file"

def read_from(fh, num):
    """Reads num lines from the open filehandle fh.  Returns lines as a list.
    Assumes fh is open and contains at least num lines from current offset"""
    return [fh.readline() for i in xrange(num)]

def permute(s, indices):
    """Permutes a string based on the indices passed."""
    p_str = ''
    idx = 0
    slen = len(s)
    ilen = len(indices)
    while idx < slen:
        block = s[idx:idx+ilen]
        for i in indices:
            p_str += block[i]
        idx += ilen
    return p_str

def rle_count(s, indices):
    """Permute then count # of changes."""
    p_str = permute(s, indices)
    count = 0
    prev_c = ''
    for c in p_str:
        if prev_c != c: 
            count += 1
        prev_c = c
    return count

def gen_all_perms(a):
    """Generator that yields all permutations of list passed."""
    if len(a) <= 1: 
        yield a
    else:
        for p in gen_all_perms(a[1:]):
            for i in range(len(p)+1):
                yield p[:i] + a[0:1] + p[i:]

def find_perm(s, k):
    """Determines minimal permutation for string given block length k."""
    #inelegant brute-force try.  Would only work for small k
    min_count = len(s)
    min_perm = range(k)
    for p in gen_all_perms(range(k)):
        count = rle_count(s, p)
        if count < min_count:
            min_count = count
            min_perm = p
    return min_count

def main(args):
    """Point of code entry.  Command name in args[0], any additional args
    passed are in the remainder of the args array."""
    if len(args) < 2:
        useage()
        return 1
    num_cases = -1
    try:
        f = open(args[1])
        num_cases = int(f.readline())
        for case in xrange(num_cases):
            k = int(f.readline())
            S = f.readline().rstrip()
            count = find_perm(S, k)
            print "Case #" + str(case+1) + ": " + str(count)
    except IOError:
        print "Invalid file input"
        useage()
        return 2

if __name__ == '__main__':
    sys.exit(main(sys.argv))
