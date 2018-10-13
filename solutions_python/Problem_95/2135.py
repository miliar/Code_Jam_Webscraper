#!/usr/bin/python

cipher = {'a': "y",
          'b': "h",
          'c': "e",
          'd': "s",
          'e': "o",
          'f': "c",
          'g': "v",
          'h': "x",
          'i': "d",
          'j': "u",
          'k': "i",
          'l': "g",
          'm': "l",
          'n': "b",
          'o': "k",
          'p': "r",
          'q': "z",
          'r': "t",
          's': "n",
          't': "w",
          'u': "j",
          'v': "p",
          'w': "f",
          'x': "m",
          'y': "a",
          'z': "q"}

import sys
numberOfLines = int(sys.stdin.readline())

for i in range(numberOfLines):
    inputLine = sys.stdin.readline().strip()
    
    outputLine = "";
    for c in inputLine:
        if (cipher.has_key(c)):
            outputLine += cipher[c]
        else:
            outputLine += c
    print "Case #%s: %s" % (i+1, outputLine)
