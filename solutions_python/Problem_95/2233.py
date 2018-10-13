# -*- coding:utf-8 -*-
'''
Created on 2012/04/14

@author: mutouyutaka
'''


import sys

MAPPING = {
    'a' :'y',
    'b' :'h',
    'c' :'e',
    'd' :'s',
    'e' :'o',
    'f' :'c',
    'g' :'v',
    'h' :'x',
    'i' :'d',
    'j' :'u',
    'k' :'i',
    'l' :'g',
    'm' :'l',
    'n' :'b',
    'o' :'k',
    'p' :'r',
    'q' :'z',
    'r' :'t',
    's' :'n',
    't' :'w',
    'u' :'j',
    'v' :'p',
    'w' :'f',
    'x' :'m',
    'y' :'a',
    'z' :'q',
}

def main() :
    lineNum   = sys.stdin.readline()
    lineNum   = int(lineNum)
    
    for i in range(0, lineNum) :
        data = sys.stdin.readline()
        data = data.strip()
        line = ''
        for j in xrange(len(data)):
            k = data[j]
            if k == ' ':
                after = ' '
            else:
                after = MAPPING[k]
            line += after
        print "Case #%s: %s" % (i + 1, line)


main()
