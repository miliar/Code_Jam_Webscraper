import sys
from pprint import pprint

def main():
    (LL,DD,NN) = tuple([int(x) for x in sys.stdin.readline().split()])
    words = []
    for d in xrange(DD):
        words.append(sys.stdin.readline().strip())
    for n in xrange(NN):
        pattern = sys.stdin.readline().strip()
        tokens = []
        i = 0
        while i < len(pattern):
            if pattern[i] == '(':
                token = ''
                i += 1
                while pattern[i] != ')':
                    token += pattern[i]
                    i += 1
                tokens.append(token)
            else:
                tokens.append(pattern[i])
            i += 1
        wordsleft = set(words)
        for l in xrange(LL):
            token = tokens[l]
            keepwords = set([])
            for i in xrange(len(token)):
                for word in wordsleft:
                    if word[l] == token[i]:
                        keepwords.add(word)
            wordsleft = keepwords
            if len(wordsleft) == 0:
                break
        print 'Case #%d: %d' % (n + 1, len(wordsleft))

if __name__ == "__main__":
    main()
