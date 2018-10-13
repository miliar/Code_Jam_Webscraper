#!/usr/bin/python

import fileinput

m = {
    ' ':' ',
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
}

i = 1
for line in fileinput.input():
    if fileinput.isfirstline():
        continue

    print "Case #" + str(i) + ":",
    i += 1
    s = ''
    for c in line.rstrip():
        s += m[c] 
    print s

