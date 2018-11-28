#!/usr/bin/env python

import sys

def main():
    trans = {'a':'y',
             'b':'h',
             'c':'e',
             'd':'s',
             'e':'o',
             'f':'c',
             'g':'v',
             'h':'x',
             'i':'d',
             'j':'u',
             'k':'i',
             'l':'g',
             'm':'l',
             'n':'b',
             'o':'k',
             'p':'r',
             'q':'z',
             'r':'t',
             's':'n',
             't':'w',
             'u':'j',
             'v':'p',
             'w':'f',
             'x':'m',
             'y':'a',
             'z':'q',
             ' ':' '}
    f = open(sys.argv[1], 'r')
    num_cases = int(f.readline().strip())
    count = 0
    for line in f:
        count += 1
        new_line = [trans[x] for x in line.strip()]
        print 'Case #%d: %s' % (count, ''.join(new_line))
    f.close()

if __name__ == '__main__':
    main()
