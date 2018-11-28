import sys

mapping = {'y': 'a',
           'n': 'b',
           'f': 'c',
           'i': 'd',
           'c': 'e',
           'w': 'f',
           'l': 'g',
           'b': 'h',
           'k': 'i',
           'u': 'j',
           'o': 'k',
           'm': 'l',
           'x': 'm',
           's': 'n',
           'e': 'o',
           'v': 'p',
           'z': 'q',
           'p': 'r',
           'd': 's',
           'r': 't',
           'j': 'u',
           'g': 'v',
           't': 'w',
           'h': 'x',
           'a': 'y',
           'q': 'z',
           ' ': ' ',
           '\n': '\n'
           }

f = open('A-small-attempt1.in', 'r')
num = int(f.readline())

count = 1

for line in f:
    sys.stdout.write('Case #%d: ' % count)
    for char in line:
        sys.stdout.write(mapping[char])
    count += 1

