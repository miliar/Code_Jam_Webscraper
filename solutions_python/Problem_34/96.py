#!/usr/bin/python
import sys

class Trie:
    def __init__(self):
        self.kids = {}
        self.valid = 0

    def insert(self, word):
        p = self
        for c in word:
            if c in p.kids:
                p = p.kids[c]
            else:
                p.kids[c] = Trie()
                p = p.kids[c]
        p.valid = 1

    def go(self, c):
        if c in self.kids:
            return self.kids[c]
        return None

def solve(input, trie):
    if trie is None: return 0
    if len(input) == 0: return trie.valid

    if input[0] == '(':
        i = input.find(')')
        variants = input[1:i]
        rest = input[i+1:]
        return sum([solve(rest, trie.go(c)) for c in variants])
    else:
        return solve(input[1:], trie.go(input[0]))

def main():
    L, D, N = map(int, sys.stdin.readline().split())
    T = Trie()

    for each in range(D):
        word = sys.stdin.readline().strip()
        assert len(word) == L
        T.insert(word)

    for cs in range(1, N+1):
        input = sys.stdin.readline().strip()
        res = solve(input, T)
        print "Case #%d: %s" % (cs, res)

main()
