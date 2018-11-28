import sys

class Trie:

    def __init__(self, prefix = ''):
        self.prefix = prefix
        self.children = {}

    def add(self, word):
        if not len(word):
            return

        head = word[0]
        tail = word[1:]

        if not head in self.children:
            subtrie = Trie(head)
            subtrie.add(tail)

            self.children[head] = subtrie
        else:
            self.get(head).add(tail)

    def get(self, prefix):
        return self.children.get(prefix)


def nextline():
    return sys.stdin.readline().rstrip()

def init():
    words = Trie()

    words.add('abc')
    words.add('bca')
    words.add('cba')
    words.add('dbc')
    words.add('dac')

    return words


def parse(s):
    return parse_with_list(s, [])

def parse_with_list(p_s, p_l=[]):
    if not len(p_s):
        return p_l

    head = p_s[0]

    if head == '(':
        pos = p_s.index(')')
        p_l.append(p_s[1:pos])
        return parse_with_list(p_s[pos+1:], p_l)
    else:
        p_l.append(head)
        return parse_with_list(p_s[1:], p_l)

def search(words, pattern):
    if words is None:
        return 0

    if not len(pattern):
        return 1

    head = pattern[0]

    return sum([search(words.get(c), pattern[1:]) for c in head])

def doMain():
    words = Trie()

    (l, d, n) = map(int, nextline().split(' '))

    for i in xrange(0, d):
        word = nextline()
        words.add(word)

    for i in xrange(0, n):
        pattern = parse(nextline())
        count = search(words, pattern)
        print "Case #%s: %s" % (i + 1, count)

if __name__ == "__main__":
    doMain()

