#!/usr/bin/python

import sys

def parseline(toks):
    toks = toks[1:-1]
    val = toks[0]
    if not toks[1:]:
        return [float(val)]
    cmp = toks[1]
    depth = 0
    vals = []
    lst = []
    for tok in toks[2:]:
        if tok == '(':
            depth += 1
        elif tok == ')':
            depth -= 1
        lst.append(tok)
        if depth == 0:
            vals.append(lst)
            lst = []
    ans = [float(val), cmp]
    ans.append(map(parseline, vals))
    return ans

def parse(s):
    s = s.replace('(', ' ( ').replace(')', ' ) ')
    tokens = s.split()
    ans = parseline(tokens)
    return ans


def value(feats, tree):
    if len(tree) == 1:
        return tree[0]
    if tree[1] in feats:
        return tree[0] * value(feats, tree[2][0])
    else:
        return tree[0] * value(feats, tree[2][1])

ncase = int(raw_input())
for i in range(ncase):
    nlines = int(raw_input())
    s = []
    for k in range(nlines):
        s.append(sys.stdin.readline())
    ans = parse('\n'.join(s))
    nanimals = int(raw_input())
    print 'Case #%d:' % (i+1) 
    for k in range(nanimals):
        toks = sys.stdin.readline().split()
        feats = toks[2:]
        print '%0.8f' % value(feats, ans)
