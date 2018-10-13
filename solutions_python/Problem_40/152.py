#!/usr/bin/env python

import string

def parse(s):
    t = []
    b = s.replace('\n', ' ').replace('  ', ' ').replace('  ', ' ').replace('( ', '(').replace(' )', ')').split()
    for tok in b:
        if tok[0] in string.lowercase:
            t.append('"' + tok + '"')
        else:
            t.append(tok)
    p = eval(','.join(t))
    return p

def evaluate(tree, features, probability = 1.0):
    f = type(0.0)
    s = type('')
    t = type(())
    skip = False
    i = 0
    try:
        len(tree)
    except:
        tree = (tree,)
    while(i < len(tree)):
        elem = tree[i]
        if type(elem) == f:
            i += 1
            probability *= elem
        elif type(elem) == s:
            if elem in features:
                n = i + 1
            else:
                n = i + 2
            if type(tree[n]) != t:
                probability *= evaluate((tree[n],), features,
                        probability) / probability
                break
            else:
                probability *= evaluate(tree[n], features,
                        probability) / probability
                break
            i += 3
        elif type(elem) == t:
            probability *= evaluate(elem, features, probability)
            i += 1
        else:
            fudeu
    return probability

def main():
    N = int(raw_input())
    for count in range(N):
        L = int(raw_input())
        tree = ''
        for i in range(L):
            tree += raw_input()
        tree = parse(tree)
        A = int(raw_input())
        print 'Case #%d:' % (count + 1)
        for i in range(A):
            animal = raw_input().split()
            probability = evaluate(tree, animal[2:])
            print '%.8f' % probability

if __name__ == '__main__':
    main()

