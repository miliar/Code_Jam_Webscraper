#! /usr/bin/python

__author__ = 'Thomas "noio" van den Berg'

### IMPORTS ###

import sys

# Shortcuts

### CONSTS ###

mapping = {
    'a':'y',
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
    ' ':' '
}

### FUNCTIONS ###


### PROCESS INPUT FILE ###

f = open(sys.argv[1])
fout = open(sys.argv[1].replace('.in','.out'),'w')

T = int(f.readline())
for case in xrange(T):
    line       = f.readline().strip()
    translated = ''.join([mapping.get(l,'_') for l in line])
    print translated
    ans = translated
    fout.write('Case #%d: %s\n'%(case+1,ans))
