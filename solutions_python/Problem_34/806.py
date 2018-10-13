#!/usr/bin/env python
fp = open('in.txt', 'rU')
lines = (line.rstrip("\n") for line in fp.xreadlines())
L, D, N = [int(val) for val in lines.next().split(' ')]
trie_root = {}
for word_index in range(D):
    word = lines.next()
    node = trie_root
    for letter in word:
        node = node.setdefault(letter, {})
    node[''] = True # leaf node marker
for case_index in range(N):
    pattern = lines.next()
    nodes = [trie_root]
    multiple = False
    possible_nodes = []
    for letter in pattern:
        if letter == '(':
            multiple = True
        elif letter == ')':
            multiple = False
        else:
            for test_node in nodes:
                if letter in test_node:
                    possible_nodes.append(test_node[letter])
        if not multiple:
            nodes = possible_nodes
            possible_nodes = []
    possible_words = sum(1 for node in nodes if '' in node)
    print 'Case #%d: %d' % (case_index + 1 , possible_words)