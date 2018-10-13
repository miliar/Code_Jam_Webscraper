#!/usr/bin/env python

import sys

input = sys.stdin.readline().strip().split(" ")

l = int(input[0])
d = int(input[1])
n = int(input[2])

words = []

for i in range(d):
    words.append(sys.stdin.readline().strip())

for i in range(n):
    thisWord = sys.stdin.readline().strip()
    cursor = 0
    possibilities = []
    possibleLetters = []
    for j in range(l):
        oldPossibilities = possibilities
        possibilities = []
        possibleWords = []
        for word in words:
            possibleWords.append(word)

        possibleLetters = ""
        if thisWord[cursor] == "(":
            cursor += 1
            while thisWord[cursor] != ")":
                possibleLetters += thisWord[cursor]
                cursor += 1
            cursor += 1
        else:
            possibleLetters = thisWord[cursor]
            cursor += 1

        if j == 0:
            for letter in possibleLetters:
                possibilities.append(letter)
        else:
            for possibility in oldPossibilities:
                for letter in possibleLetters:
                    for word in possibleWords:
                        if word.startswith(possibility + letter):
                            possibilities.append(possibility + letter)
                            break

    print "Case #%d: %d" % (i+1, len(possibilities))
