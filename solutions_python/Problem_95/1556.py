import sys
import string

DICT = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u',
        'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p',
        'y': 'a', 'x': 'm', 'q': 'z', 'z': 'q'}

def char_map(ch):
    if ch in DICT:
        return DICT[ch]
    else:
        return ch

def build_map():
    dictionary = {}
    with open('input.txt', 'r') as f:
        f.readline()
        s = f.read()
    t = ''
    with open('output.txt', 'r') as f:
        for line in f:
            t += line.split(':')[1]

    s = filter(lambda x: x.isalpha(), s)
    t = filter(lambda x: x.isalpha(), t)
    return dict(zip(s, t))


def translate():
    f = sys.stdin
    line = f.readline()
    n = int(line.strip())
    for i in xrange(n):
        line = f.readline().strip()
        line = map(char_map, line)
        line = ''.join(line)
        print 'Case #%d: %s' % (i + 1, line)

if __name__ == '__main__':
    translate()