#!/usr/bin/python
from sys import argv
letters_map = {'a': 'y', 'b': 'h', 'c': 'e', 'd': 's', 'e': 'o', 'f': 'c', 
               'g': 'v', 'h': 'x', 'i': 'd', 'j': 'u', 'k': 'i', 'l': 'g',
               'm': 'l', 'n': 'b', 'o': 'k', 'p': 'r', 'q': 'z', 'r': 't',
               's': 'n', 't': 'w', 'u': 'j', 'v': 'p', 'w': 'f', 'x': 'm',
               'y': 'a', 'z': 'q',}
f = open(argv[1], "r")
x = f.readline()
i = 0
for line in f.readlines():
    i += 1
    new_line = ""
    for letter in line:
        if letter != "\n":
            if letter == " ":
                new_line += " "
            else:
               new_line += letters_map[letter]
    print "Case #%s: %s"%(i, new_line)
