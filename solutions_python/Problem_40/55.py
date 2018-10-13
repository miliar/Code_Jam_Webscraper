#!/usr/bin/env python
import sys

f = sys.stdin
n = int(f.readline())

class TreeNode(object):
    def __init__(self, text):
        assert text[0] == '(' and text[-1] == ')'
        tree = text[1:-1].strip()
        if ' ' in tree:
            weight, feature, tree = tree.split(None, 2)
            self.weight = float(weight)
            self.feature = feature
            count = 0
            for i, c in enumerate(tree):
                if c == '(':
                    count += 1
                elif c == ')':
                    count -= 1
                    if count == 0:
                        break
            self.true = TreeNode(tree[:i+1].strip())
            self.false = TreeNode(tree[i+1:].strip())
        else:
            self.weight = float(tree)
            self.feature = None

    def __repr__(self):
        if self.feature:
            return 'Decision: %f %s <%s> <%s>' % (self.weight, self.feature, self.true, self.false)
        else:
            return 'Decision: %f' % self.weight

    def evaluate(self, animal, karma):
        karma *= self.weight
        if self.feature:
            if self.feature in animal:
                return self.true.evaluate(animal, karma)
            else:
                return self.false.evaluate(animal, karma)
        return karma

for case in range(1, n + 1):
    print 'Case #%i:' % case

    l = int(f.readline())
    tree = ' '.join(f.readline().strip() for i in range(l))
    tree = TreeNode(tree)

    a = int(f.readline())
    animals = [f.readline().strip().split() for i in range(a)]
    animals = [(animal[0], animal[2:]) for animal in animals]
    print '\n'.join('%.7f' % tree.evaluate(animal[1], 1.0) for animal in animals)
