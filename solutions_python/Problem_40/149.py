#!/usr/bin/env py3k
"""A solver for GCJ 2009, Round 1B, Problem A."""
from sys import stdin
from re import split, compile
from decimal import Decimal as D

clean_regex = compile('\ +')
tree_regex = compile('\(\ *([0-9]\.*[0-9]*)\ *([a-z]*)' + \
'\ *(\(*.*\)*)')

def make_tree(tree):
    tree = clean_regex.sub(' ', tree.replace('\n', ''))
    (weight, feature, subtrees) = tree_regex.match(tree).groups()
    if subtrees.strip() == '':
        return (weight, feature, [])
    else:
        index = 0
        indent = 0
        sections = []
        for c in subtrees:
            if c == ')':
                indent -= 1
                if indent == 0:
                    sections.append(index + 1)
                index += 1
                continue
            if c == '(':
                if indent == 0:
                    sections.append(index)
                indent += 1
                index += 1
                continue
            index += 1
        sections = zip(*[iter(sections)]*2)
        subtreelist = []
        for tup in sections:
            subtreelist.append(subtrees[tup[0]:tup[1]])
        return (weight, feature, [make_tree(st) for st in subtreelist])

def probability(tree, name, features, prob):
    weight = D(tree[0])
    feature = tree[1]
    subtrees = tree[2]
    prob = prob * weight
    if len(subtrees) > 0:
        if feature in features:
            prob = probability(subtrees[0], name, features, prob)
        else:
            prob = probability(subtrees[1], name, features, prob)
    return str(D(prob).quantize(D('1.0000000')))

def probabilities(tree, animals):
    tree = make_tree(tree)
    probabilities = []
    for animal in animals.split('\n'):
        if animal.strip() != '':
            animal = animal.strip().split(' ')
            name = animal.pop(0)
            probabilities.append(probability(tree, name, animal[1:], D(1)))
    return '\n'.join(probabilities)

lines = stdin.readlines()
nocases = int(lines.pop(0))
lenfirstcase = lines.pop(0)

sections = split('\n[0-9]+\n', ''.join(lines))
cases = zip(*[iter(sections)]*2) # tree: animals

caseno = 1
for tup in cases:
    print('Case #%s:\n%s' % (caseno, probabilities(tup[0], tup[1])))
    caseno += 1