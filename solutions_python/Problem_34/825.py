#!/usr/bin/env python

import sys

class Node(object):
    def __init__(self, c):
        self.c = c
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __str__(self):
        s = self.c + ' '
        for c in self.children:
            s += c.c
        return s

def read_input(file):
    with open(file) as f:
        sizes = f.readline()
        (L, D, N) = sizes.split(' ')
        L = int(L)
        D = int(D)
        N = int(N)
        words = []
        for i in range(D):
            w = f.readline()
            w = w[:-1]
            words.append(w)
        cases = []
        for i in range(N):
            n = f.readline()
            n = n[:-1]
            cases.append(n)
    return (L, D, N, words, cases)


def build_tree(words):
    root = Node('')
    for word in words:
        add_word(word, root)
    return root

def add_word(word, node):
    if word == '':
        return
    found = False
    for child in node.children:
        if word[0] == child.c:
            found = True
            add_word(word[1:], child)
    if not found:
        new_child = Node(word[0])
        node.add_child(new_child)
        add_word(word[1:], new_child)

def matches(node, tokens, i=0):
    #print '-' * 10
    matched = 0
    #print 'tokens', tokens, node, i
    if len(tokens) == 0:
        return 1
    for token in tokens[0]:
        #print '--> ' + node.c, token
        for child in node.children:
            if child.c == token:
                #print ': ', token, child.c
                m = matches(child, tokens[1:], i+1)
                if m:
                    matched += m
    # if len(tokens) == 1:
    #     print tokens[0], matched
    return matched

def test_cases(L, root, cases):
    results = [0 for i in range(len(cases))]
    # ptrn_str = r''
    # for i in range(L):
    #     ptrn_str += r'\(?(\w+)\)?'
    # print ptrn_str
    # ptrn = re.compile(ptrn_str)
    i = 0
    for c in cases:
        tokens = []
        pos = 0
        for z in range(L):
            if c[pos] != '(':
                tokens.append(c[pos])
                pos += 1
            else:
                p_end = c.find(')', pos)
                tokens.append(c[pos + 1:p_end])
                pos = p_end + 1
        # print tokens
        # m = ptrn.match(c)
        # tokens = m.groups()
        # print tokens
        #print matches(root, tokens), c
        results[i] = matches(root, tokens)
        i += 1
    return results

            
if __name__ == '__main__':
    (L, D, N, words, cases) = read_input(sys.argv[1])
    root = build_tree(words)
    #print root
    res = test_cases(L, root, cases)
    f = open('out', 'w')
    for i in range(len(res)):
        f.write('Case #' + str(i + 1) + ': ' + str(res[i]) + '\n')
    f.close()
