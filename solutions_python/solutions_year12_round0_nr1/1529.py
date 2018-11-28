#!/usr/bin/env python

import sys

googlerese = {
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
    ' ':' ',
    '\n':'\n'
    }

if __name__ == "__main__":

    f = open("A-small-attempt3.in", 'r')
    fout = open("output", "w")
    count = int(f.readline())
    tmp = count
    while count > 0:
        line = f.readline()
        output = "Case #"
        output += str(tmp - count + 1)
        output += ": "
        for c in line:
            output += googlerese[c]
        fout.write(output)
        count -= 1
