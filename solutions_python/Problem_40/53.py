#!/usr/bin/python

import sys

class Tree:
    def __init__(self, p, feature = None):
	self.p = p
	self.feature = feature
	self.left = None
	self.right = None
    def addleft(self, left):
	self.left = left
    def addright(self, right):
	self.right = right
    def decide(self, features):
	if self.feature == None:
	    return self.p
	if self.feature in features:
	    return self.p * self.left.decide(features)
	else:
	    return self.p * self.right.decide(features)

def getToken(s):
    s = s.lstrip()
    if s == "": return None, None
    if s[0] == '(': return s[0], s[1:]
    if s[0] == ')': return s[0], s[1:]
    i = 1
    while i < len(s) and s[i] in '0123456789.abcdefghijklmnopqrstuvwxyz': i+=1
    return s[0:i], s[i:]

def parseTree(s):
    token, s = getToken(s)
    assert(token == '(')
    p, s = getToken(s)
    f, s = getToken(s)
    if f == ')':
	return Tree(float(p)), s
    left, s = parseTree(s)
    right, s = parseTree(s)
    c, s = getToken(s)
    assert(c == ')')
    t = Tree(float(p), f)
    t.addleft(left)
    t.addright(right)
    return t, s

f = open(sys.argv[1])
N = int(f.readline())
for n in range(1, N+1):
    L = int(f.readline().strip())
    s = ""
    for l in range(L):
	s += f.readline().strip()
    tree, s = parseTree(s)
    assert(s.strip() == "")
    A = int(f.readline().strip())
    print 'Case #%d:' % n
    for a in range(A):
	fields = f.readline().strip().split()
	animal = fields[0]
	features = fields[2:]
	p = tree.decide(features)
	print '%.7f' % p
