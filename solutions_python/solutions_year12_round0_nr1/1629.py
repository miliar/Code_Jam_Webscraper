#!/usr/bin/python

import sys


def build_dict(fname_in, fname_out):
    f1 = open(fname_in, 'r')
    f2 = open(fname_out, 'r')
    inp = f1.readlines()[1:]
    oup = f2.readlines()
    f1.close()
    f2.close()

    inp = map(lambda x: x[:-1], inp)
    oup = map(lambda x: x[x.find(':')+2:-1], oup)

    d = {}
    l = 0
    while l < len(inp):
        i = 0
        l1 = inp[l]
        l2 = oup[l]
        while i < len(l1):
            d[l1[i]] = l2[i]
            i += 1
        l += 1

    return d


def check_dict(d):
    l = "abcdefghijklmnopqrstuvwxyz"
    for letter in l:
        if not d.has_key(letter):
            print letter, "missing"


def swap(line, d):
    ret = ""
    for letter in line:
        ret += d[letter]
    return ret


def solve_input(fname, d):
    f = open(fname, 'r')
    f.readline()
    i = 1
    for line in f:
        print "Case #" + str(i) + ": " + swap(line[:-1], d)
        i += 1
    f.close()


if __name__ == "__main__":
    d = build_dict('sample', 'sample_output')

    #-------------------
    d['q'] = 'z'
    d['z'] = 'q'
    #-------------------
    # d['q'] = 'q'
    # d['z'] = 'z'

    if len(sys.argv) == 2:
        fname = sys.argv[1]
    else:
        fname = 'sample'

    solve_input(fname, d)
