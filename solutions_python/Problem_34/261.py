import sys
import re

token_regex = re.compile(r"(([a-z])|\(([a-z]+)\))(.*)")
def tokenize(word):
    m = token_regex.match(word)
    if m:
        t, c, g, rest = m.groups()
        if c:
            return [[c]] + tokenize(rest)
        else:
            return [sorted(g)] + tokenize(rest)
    else:
        return []


def parse_ints(line):
    return map(int, line.split())

class Trie(object):
    def __init__(self):
        self.value = None
        self.children = [None] * 26

    def ord(self, char):
        return ord(char) - ord('a')

    def insert(self, s, value):
        if not s:
            self.value = value
        else:
            i = self.ord(s[0])
            if not self.children[i]:
                self.children[i] = Trie()
            self.children[i].insert(s[1:], value)

    def search(self, s):
        if not s:
            return self.value
        else:
            child = self.children[self.ord(s[0])]
            return child.search(s[1:]) if child else 0

    def count(self, case):
        if case:
            children = [self.children[self.ord(x)] for x in case[0]]
            return sum([x.count(case[1:]) if x else 0 for x in children])
        else:
            return self.value

if __name__ == "__main__":
    lines = sys.stdin.readlines()

    l, d, n = parse_ints(lines[0])

    t = Trie()
    for w in [word.strip() for word in lines[1:d+1]]:
        t.insert(w,1)

    cases = [tokenize(case.strip()) for case in lines[d+1:]]
    for x,case in enumerate(cases):
        print "Case #%d: %d" % (x+1, t.count(case))
