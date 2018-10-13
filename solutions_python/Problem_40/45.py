#!/usr/bin/env python

class Tree(object):
    def __init__(self, subtree):
        self.weight = float(subtree[0])

        if len(subtree) == 1:
            self.feature = None
            self.left = None
            self.right = None
            return

        self.feature = subtree[1]

        count = 1
        pos = 3
        while count > 0:
            if subtree[pos] == '(':
                count += 1
            elif subtree[pos] == ')':
                count -= 1
            pos += 1

        self.left = Tree(subtree[3:pos-1])
        self.right = Tree(subtree[pos+1:-1])
        

def walk(node, animal, features, p=1.0):
    p *= node.weight

    if node.feature is None:
        return p

    if node.feature in features:
        return walk(node.left, animal, features, p)
    else:
        return walk(node.right, animal, features, p)

probs = {}

def quick_walk(node, animals, features, p=1.0):
    p *= node.weight

    if node.feature is None:
        for animal in animals:
            probs[animal] = p
        return

    left = features.get(node.feature, set()).intersection(animals)
    right = animals - left
    quick_walk(node.left, left, features, p)
    quick_walk(node.right, right, features, p)


readline = lambda : raw_input()
#f = file('A-sample.in')
#readline = lambda : f.readline()

N = int(readline())

for n in range(N):
    L = int(readline())
    treestr = ' '.join(readline().strip() for i in range(L)).strip()
    A = int(readline())
    animals = []
    for a in range(A):
        splitted = readline().split()
        animals.append((splitted[0], set(splitted[2:])))

    treestr = treestr[1:-1].replace('(', ' ( ').replace(')', ' ) ')
    root = Tree(treestr.split())

    print "Case #%d:" % (n+1)

    features = {}
    probs.clear()
    anis = []
    for animal, fs in animals:
        anis.append(animal)
        for ff in fs:
            if ff in features:
                features[ff].add(animal)
            else:
                features[ff] = set([animal])

    quick_walk(root, set(anis), features)

    for animal in animals:
        print '%.7f' % probs[animal[0]]
