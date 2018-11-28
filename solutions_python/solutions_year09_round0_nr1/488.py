#!/usr/bin/env python
import sys

l, n, d = map(int, sys.stdin.readline().split(" ")) 

#print "l, n, d: %s"%[l,n,d]
trie = {}
words = []
for i in xrange(n):
    word = sys.stdin.readline()
    words += [word]
    node = trie
    for j in xrange(l):
        if word[j] not in node:
            node[word[j]] = {}
        node = node[word[j]]

#print "words: %s"%words
#print "trie: %s"%trie

for i in xrange(d):
    pattern = sys.stdin.readline().strip()
    #print "pattern: %s" % pattern
    nodes = [trie]
    #for frag in pattern.split(')'):
    multi = False
    newnodes = []
    for letter in pattern:
        if letter=="(":
            multi = True 
            continue
        if letter==")":
            multi = False
            nodes = newnodes
            newnodes = []
            continue
    #    print "letter: %s, multi? %s, nodes: %s"%(letter,multi,nodes)
        for node in nodes:
            if letter in node:
                #print "node = %s, frag[j] = %s, node[frag[j]] = %s"%(node, frag[j], node[frag[j]])
                newnodes += [node[letter]]
        if not multi:
            nodes = newnodes
            newnodes = []
        if len(nodes)==0:
            break 
    print "Case #%d: %d"%(i+1, len(nodes))
   # sys.exit()
