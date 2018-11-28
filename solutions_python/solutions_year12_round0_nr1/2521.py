#!/usr/bin/env python

def degoogle(line):
    chars = {'\n': '\n', ' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}
    output = []

    for ch in line:
        output.extend(chars[ch])

    return ''.join(output)

sample = open("sample","r")
sample.readline()

i=1
for line in sample:
    output = degoogle(line)
    print "Case #%i: %s" % (i, output),
    i = i + 1
