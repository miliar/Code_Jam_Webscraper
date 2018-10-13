#!/usr/bin/env python
# GABRIEL PETTIER
#jeudi 3 septembre 2009, 13:03:46 (UTC+0200)

class language(object):
    def __init__(self, length):
        self.voc = {}
        self.length = length

    def add(self, word, tree=None):
        if tree is None: tree = self.voc
        if len(word) != 0:
            if word[0] not in tree.keys():
                tree[word[0]] = {}
            self.add(word[1:], tree=tree[word[0]])
            #print tree[word[0]]

    def solve(self, i, tree=None):
        if tree is None: tree = self.voc
        ret = 0
        if len(i) == 0:
            return 1
        else:
            for c in i[0]:
                if c in tree.keys():
                    ret += self.solve(i[1:], tree[c])
        return ret

file = open('A-small.in')
L, D, N = [int(i) for i in file.readline().split('\n')[0].split(' ')]
l = language(L)

for i in range(D):
    line = file.readline()
    l.add(line.split('\n')[0])

inputs = []
n=0
for line in file.readlines():
    pattern = []
    i = 0
    while line[i] != '\n':
        if line[i] == '(':
            i += 1
            t = []
            while line[i] != ')':
                t.append(line[i])
                i += 1
        else:
            t = [line[i]]
        i += 1
        pattern.append(t)
    n+=1
    print 'Case #'+str(n)+': '+str(l.solve(pattern))


