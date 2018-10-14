from __future__ import with_statement
import sys

def veryWelcome(search, string, n):

    if len(search) == 0:
        return n + 1
    
    if len(string) < len(search):
        return n
    
    if search[0] == string[0]:
        n = veryWelcome(search[1:], string[1:], n)
    
    string = string[1:]
    n = veryWelcome(search, string, n)
    return n

w = open(sys.argv[1].replace("in", "out"), 'w')

with open(sys.argv[1]) as f:
    i = False
    for line in f:
        if not i:
            i = 1
        else:
            w.write("Case #%(i)s: %(#)04d\n" % {"i": i, "#": veryWelcome("welcome to code jam", line, 0)})
            i += 1
