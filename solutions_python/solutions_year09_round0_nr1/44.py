#!/usr/bin/env python

from __future__ import with_statement

def valid(s, leaf, tot = 0):
    #print s, leaf, tot
    if leaf == {}:
	#print "1"
	return 1 + tot
    if s[0] == '(':
	rp = s.find(')')
	for c in range(1, rp):
	    tot = valid(s[c] + s[rp+1:], leaf, tot)
    else:
	if s[0] in leaf:
	    leaf = leaf[s[0]]
	    tot = valid(s[1:], leaf, tot)
    return tot

def processFile(fname):

    f = open("answer_" + fname, "w")
    
    with open(fname, "r") as data:
        l, d, n = map(int, data.readline().strip("\n").split(" "))
	tree = {}
	for i in range(d):
	    leaf = tree
	    word = data.readline().strip("\n")
	    for j in range(l):
		if word[j] in leaf:
		    leaf[word[j]].update({})
		else:
		    leaf[word[j]] = {}
		leaf = leaf[word[j]]

	for i in range(n):
	    test = data.readline().strip("\n")
	    count = 0
	    #print test
	    count = valid(test, tree)
	    f.write("Case #%d: %d\n" % (i + 1, count))

    f.close()
processFile("A-large.in")

#processFile("C-small-practice.in")
