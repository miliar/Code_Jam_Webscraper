import sys

x = {' ': ' ',\
        'a': 'y',\
        'b': 'h',\
        'c': 'e',\
        'd': 's',\
        'e': 'o',\
        'f': 'c',\
        'g': 'v',\
        'h': 'x',\
        'i': 'd',\
        'j': 'u',\
        'k': 'i',\
        'l': 'g',\
        'm': 'l',\
        'n': 'b',\
        'o': 'k',\
        'p': 'r',\
        'q': 'z',\
        'r': 't',\
        's': 'n',\
        't': 'w',\
        'u': 'j',\
        'v': 'p',\
        'w': 'f',\
        'x': 'm',\
        'y': 'a',\
        'z': 'q'}

def decipher(s):
    return ''.join(map(lambda y: x[y], s))

count = 1
#sys.stdin.read()
for line in sys.stdin:
    print 'Case #%d: %s' % (count, decipher(line[:-1]))
    count += 1

