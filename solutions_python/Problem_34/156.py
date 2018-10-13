#!/usr/bin/env python
# chteo@gcj09::0::A

from sys import argv

# add string to a Trie ie. a dict of dict of dict...
def add(T,s):
    while len(s) != 0:
        T = T.setdefault(s[0],{})
        s = s[1:]

# tokenize test word into list of (groups of) alphabets
def tokenize(s):
    la = []
    while len(s) > 0:
        if s[0] == '(':
            e = s.index(')')
            la.append(s[1:e])
            s = s[e+1:]
        else:
            la.append(s[0])
            s = s[1:]
    return la

# depth-first traverse Trie and count the magic number!
def dfs(T,la):
    if len(T) == 0:
        # reach Trie leaf then found exact match
        return 1
    elif len(la) == 0:
        # not likely but for safety
        return 0
    else:
        # keep branching and counting...
        cnt = 0
        for t in la[0]:
            if t in T:
                cnt += dfs(T[t],la[1:])
        return cnt


# print Trie recursively via Depth First Traversal
def print_trie(T,sofar):
    if len(T) == 0:
        print sofar
    else:
        for t in T:
            print_trie(T[t],sofar+t)


f = open(argv[1])
l = f.readline().strip().split()
L,D,N = map(eval,l)

# build Trie
T = {}
for i in range(D):
    add(T,f.readline().strip())

#print_trie(T,'')

# run test cases
for i in range(N):
    l  = f.readline().strip()
    la = tokenize(l) 
    cnt = dfs(T,la)
    print 'Case #%d: %d' % (i+1,cnt)
    


