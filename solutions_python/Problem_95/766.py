# -*- coding:utf-8 -*-
import os
basepath = '/Users/voidus/Documents/workspace/xp/jam/files/trans'

srcfilename = os.path.join(basepath, 'A-small-attempt0.in')
dstfilename = os.path.join(basepath, 'A-small-attempt0.out.txt')

table = {
    ' ': ' ',
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
    '\r': '\r',
    '\n': '\n'
}
import string
from_ = ''
to_ = ''
for key, value in table.items():
    from_ += key
    to_ += value 
    
trans = string.maketrans(from_, to_)

if __name__ == '__main__':
    with open(srcfilename, 'rb') as inp:
        with open(dstfilename, 'wb') as outp:
            lines = inp.readlines()
            count = int(lines.pop(0))
            outlines = []
            for i in xrange(count):
                line = lines[i]
                decoded = line.translate(trans) 
                outlines.append('Case #%d: %s' % (i+1, decoded))
            outp.writelines(outlines)
