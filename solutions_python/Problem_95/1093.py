import sys

d = {' ': ' ',
 'A': 'Y',
 'B': 'H',
 'C': 'E',
 'D': 'S',
 'E': 'O',
 'F': 'C',
 'G': 'V',
 'H': 'X',
 'I': 'D',
 'J': 'U',
 'K': 'I',
 'L': 'G',
 'M': 'L',
 'N': 'B',
 'O': 'K',
 'P': 'R',
 'Q': 'Z',
 'R': 'T',
 'S': 'N',
 'T': 'W',
 'U': 'J',
 'V': 'P',
 'W': 'F',
 'X': 'M',
 'Y': 'A',
 'Z': 'Q',
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
 'z': 'q'}

def dec(n, l):
    print 'Case #%d:'%n,
    print ''.join(map(lambda c:d[c], l))

f = sys.stdin
n = int(f.readline())
for i in range(n):
    l = f.readline().rstrip()
    dec(i+1, l)

