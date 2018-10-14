#!/usr/bin/env python

#infile = file("test.in")
infile = file("small.in")
#infile = file("big.in")

code = dict()
for i, j in zip("ynficwlbkuomxsevzpdrjgthaq", "abcdefghijklmnopqrstuvwxyz"):
    code[i] = j
code[' '] = ' '
code['\n'] = ''

T = int(infile.readline())
for i in range(1, T+1):
    string = infile.readline()
    english = [code[j] for j in string]
    print("Case #{}: {}".format(i, "".join(english)))

