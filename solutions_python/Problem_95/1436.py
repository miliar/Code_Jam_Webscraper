#!/usr/bin/env python

from string import maketrans
from sys import stdin, stdout

if __name__ == '__main__':
    intab   = 'abcdefghijklmnopqrstuvwxyz'
    outtab  = 'yhesocvxduiglbkrztnwjpfmaq'
    trantab = maketrans(intab, outtab)

    T = int(stdin.readline())
    for t in range(T):
        line = stdin.readline()
        stdout.write('Case #%d: %s' % (t + 1, line.translate(trantab)))

