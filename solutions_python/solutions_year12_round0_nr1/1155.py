#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      wani
#
# Created:     14/04/2012
# Copyright:   (c) wani 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import sys
import copy

dic = {'a': 'y',
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
'z': 'q'}

def translate(sentence):
    ans = ""
    for s in sentence:
        if s == " ":
            ans += s
        else:
            ans += dic[s]
    return ans

def main():
    f = open(sys.argv[1])
    fo = open(sys.argv[2],"w")

    cases = int(f.readline().strip())
    for i in range(cases):
        s = f.readline().strip()
        out = "Case #%d: %s"%(i+1,translate(s)) + "\n"
        print out,
        fo.write(out)
    f.close()
    fo.close()

if __name__ == '__main__':
    main()
