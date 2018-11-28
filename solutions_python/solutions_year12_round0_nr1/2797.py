#!/usr/bin/python
import fileinput
import sys

tr = {
        'y':'a',
        'n':'b',
        'f':'c',
        'i':'d',
        'c':'e',
        'w':'f',
        'l':'g',
        'b':'h',
        'k':'i',
        'u':'j',
        'o':'k',
        'm':'l',
        'x':'m',
        's':'n',
        'e':'o',
        'v':'p',
        'z':'q',
        'p':'r',
        'd':'s',
        'r':'t',
        'j':'u',
        'g':'v',
        't':'w',
        'h':'x',
        'a':'y',
        'q':'z',
}

lines = [line for line in fileinput.input()][1::]
case = 1
for line in lines:
    sys.stdout.write('Case #%d: ' % case)
    for c in line:
        if c in tr:
            sys.stdout.write(tr[c])
        else:
            sys.stdout.write(c)
    case += 1

