#!/usr/bin/env python
fname = "A-large.in"
f = open(fname, 'r')

#L is length of each word
#D is size of dictionary
#N is number of test cases

line = f.next()
L, D, N = [int(n) for n in line.split()]

words = []
for eachline in range(D):
    line = f.next()
    words.append(str.strip(line))

#create potential chars
patterns = []
for eachpattern in range(N):
    c = 0
    line = f.next()
    #match pattern with dictionary
    potentials = []
    for character in range(L):
        #either brackets,or not
        if line[c] == '(':
            c+=1
            group = []
            while line[c] != ')':
                group += line[c]
                c+=1
            potentials.append(group)
        else:
            potentials.append([line[c]])
        c+=1
    patterns.append(potentials)

#match on dictionary
counts = []
for p, pattern in enumerate(patterns):
    counts += [0]
    for w, word in enumerate(words):
        if all([word[i] in pattern[i] for i in range(L)]):
            counts[p]+=1
        
for i, c in enumerate(counts):
    print 'Case #%d: %d' % (i+1, c)
        
        

