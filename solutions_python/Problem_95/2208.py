#!/usr/bin/env python
import sys

mapping = {
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

test_size = int(sys.stdin.readline())

for x in range(1, test_size+1):
    line = sys.stdin.readline().strip()
    s = ""
    for c in line:
        s += mapping[c]
    print "Case #%d: %s" % (x, s)

