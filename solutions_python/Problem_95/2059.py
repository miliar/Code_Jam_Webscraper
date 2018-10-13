import sys

mapping = {
    'a': 'y',
    'b': 'h',
    'c': 'e',
    'd': 's',
    'e': 'o',
    'f': 'c',
    'g': 'v',
    'h': 'x',
    'i': 'd',
    'j': 'u',
    'k': 'i',
    'l': 'g',
    'm': 'l',
    'n': 'b',
    'o': 'k',
    'p': 'r',
    'q': 'z',
    'r': 't',
    's': 'n',
    't': 'w',
    'u': 'j',
    'v': 'p',
    'w': 'f',
    'x': 'm',
    'y': 'a',
    'z': 'q',
    ' ': ' ',
    '\n': '\n',
    '\r': '\r',
}

f = open('A-small-attempt0.in', 'r')

case = -1
for line in f:
    case += 1
    if case == 0:
        continue

    sys.stdout.write('Case #' + str(case) + ': ')
    for char in line:
        sys.stdout.write(mapping[char])
