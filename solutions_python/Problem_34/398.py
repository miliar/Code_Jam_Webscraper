import sys


def parse(string):
    paren = False
    group = ''
    for char in string:
        if char is '(':
            assert not paren
            paren = True
        elif char is ')':
            assert paren
            paren = False
            if group:
                yield group
                group = ''
        elif paren:
            group += char
        else:
            yield char
    assert not paren
    if group:
        yield group


def test_case(handle, lexicon):
    return lexicon.sum(tuple(parse(handle.next().strip())))


class Trie:
    def __init__(self):
        self.children = {}
        self.end = False

    def put(self, s):
        if not s:
            self.end = True
            return
        c, s = s[0], s[1:]
        child = self.children.get(c)
        if child is None:
            child = self.children[c] = Trie()
        child.put(s)

    def sum(self, pattern):
        if not pattern:
            if self.end:
                return 1
        total = 0
        for c in pattern[0]:
            child = self.children.get(c)
            if child:
                total += child.sum(pattern[1:])
        return total


def run(handle):
    l, d, n = map(int, handle.next().strip().split())

    lexicon = Trie()
    for _ in xrange(d):
        lexicon.put(handle.next().strip())

    for i in xrange(n):
        print 'Case #%d: %d' % (i+1, test_case(handle, lexicon))


if __name__ == '__main__':
    run(sys.stdin)
