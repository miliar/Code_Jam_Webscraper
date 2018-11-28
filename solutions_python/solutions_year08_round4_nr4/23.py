#!/usr/bin/env python

import sys

def all_perms(str):
    if len(str) <=1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]

def compress_size(s):
    changes = 0
    last = None
    for i in s:
        if i!=last:
            changes = changes+1
            last = i
    return changes

#print compress_size("aabcaaaa")

def permute_block(b, p):
    s = list(b)
    for i,v in enumerate(p):
        s[v] = b[i]
    return ''.join(s)

def permute_repeated(b, p):
    s = []
    for i in range(0,len(b),len(p)):
        s.append(permute_block(b[i:i+len(p)], p))
    return ''.join(s)

def do_trial(f):
    k = int(f.readline())
    s = f.readline()[:-1]
    m = compress_size(s)
    for p in all_perms(range(k)):
        m = min(m, compress_size(permute_repeated(s, p)))
    return m

f = sys.stdin
#f = file("tiny.in")
count = int(f.readline())
for i in range(count):
    r = do_trial(f)
    print "Case #%d: %s" % (i+1, r)
