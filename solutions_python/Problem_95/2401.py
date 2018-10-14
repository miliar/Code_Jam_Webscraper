import string

ifn = 'A-small-attempt0.in'
ofn = 'A-small-attempt0.out'

dict = {
    ' ': ' ', '\n': '\n', '\r': '\r', '\t': '\t',
    'a': 'y', 'b': 'h', 'c': 'e', 'd': 's', 'e': 'o',                                        
    'f': 'c', 'g': 'v', 'h': 'x', 'i': 'd', 'j': 'u',
    'k': 'i', 'l': 'g', 'm': 'l', 'n': 'b', 'o': 'k',
    'p': 'r', 'q': 'z', 'r': 't', 's': 'n', 't': 'w',
    'u': 'j', 'v': 'p', 'w': 'f', 'x': 'm',
    'y': 'a', 'z': 'q'
    }
out_f = open(ofn, 'w')

with open(ifn, 'r') as in_f:
    n = int(in_f.readline())
    for i in range(0, n):
        decrypt = ''
        line = in_f.readline()
        for letter in line:
            decrypt += dict[letter]
        out_f.write('Case #%d: %s' % (i+1, decrypt))
    out_f.close()

