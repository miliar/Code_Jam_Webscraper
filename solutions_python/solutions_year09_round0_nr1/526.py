#!/usr/bin/env python
import re

# tree: [parent, child1, child2, ...]

def insert(tree, word):
    for ancestor in tree[1:]:
        if word[0] == ancestor[0]:
            insert(ancestor, word[1:])
            break
    else:
        tree.append(make_tree(word))

def make_tree(word):
    if len(word) == 1:
        return [word]
    else:
        return [word[0]] + [make_tree(word[1:])]

def accept(tree, case):
    debug("tree %s %s" % (tree, case))
    if len(tree) == 0:
        if len(case) == 0:
            debug("!! accepted")
            return 1   # accepted
        else:
            debug("!! rejected")
            return 0

    if case[0] == "(":
        m = re.compile(r"\(([^)]+)\)(.*)").match(case)
        head = m.group(1)
        rest = m.group(2)
        debug([x + rest for x in head])
        return sum([accept(tree, x + rest) for x in head])
    else:
        head = case[0]
        rest = case[1:]
        for ancestor in tree:
            if ancestor[0] == head:
                return accept(ancestor[1:], rest)
        debug("!! rejected")
        return 0

def debug(str):
    if DEBUG == 1:
        print(str)

#
# main routine
#
DEBUG = 0

L, D, N = [int(n) for n in raw_input().split()]
debug("L, D, N = %d, %d, %d" % (L, D, N))

tree = []
for i in range(D):
    word = raw_input()
    debug("got " + word)
    insert(tree, word)
    debug(tree)

for i in range(N):
    case = raw_input()
    debug("try " + case)
    n = accept(tree, case)
    print("Case #%d: %d" % (i + 1, n))
