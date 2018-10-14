import os

def addpath(e, existspath):
    es = e[1:].split("/")
    onepath = "" 
    for p in es:
        onepath = "%s/%s" % (onepath, p) 
        existspath.append(onepath)

def calc(n, m, exists, create):
    n = 0
    existspath = []
    for e in exists:
        addpath(e, existspath)
    for c in create:
        cs = c[1:].split("/")
        onepath = "" 
        for p in cs:
            onepath = "%s/%s" % (onepath, p) 
            if onepath not in existspath:
                n = n + 1
                existspath.append(onepath)
    return n

t = input()

for i in xrange(t):
    n, m = map(int, raw_input().split())
    print "Case #%d:" % (i+1),
    exists = []
    for j in xrange(n):
        exists.append(raw_input())
    create = []
    for k in xrange(m):
        create.append(raw_input())
    print calc(n, m, exists, create)
    