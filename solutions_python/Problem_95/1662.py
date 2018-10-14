#!/usr/bin/env python

import sys

def parseInput(inputfile):
    lines = [item.strip() for item in open(inputfile).readlines()]
    t = int(lines[0])
    cases = lines[1:]
    return (t, cases)

def printResult(case, result):
    print("Case #%s: %s" % (case,result))

gdict = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 
        'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 
        'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 
        't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

def translate(sentence):
    result = []
    for letter in sentence:
        if letter.isupper():
            translation = (gdict[letter.lower()]).upper()
        else:
            translation = gdict[letter]
        result.append(translation)

    result = ''.join(result)
    return result

inputfile = sys.argv[1]
t, sentences = parseInput(inputfile)
for index in range(1,t+1):
    sentence = sentences[index-1]
    printResult(index, translate(sentence))
