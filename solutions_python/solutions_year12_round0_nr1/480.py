#!/bin/python
#default gcj in file reader
#Boreeas, 7/3/2012
fin = open("in")
fout = open("out", "w")
case = 0
letterMapping = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o',
                 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x',
                 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k',
                 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't',
                 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a',
                 'x': 'm', 'z': 'q'}


def wrt(out):
    global case
    case += 1
    fout.write("Case #" + str(case) + ": " + str(out) + "\n")

fin.readline()  #skip number-of-cases
while 1:
    line = fin.readline().rstrip()
    if not line:
        break
    newtext = ""
    for letter in line:
        newtext += letterMapping[letter]

    wrt(newtext)

#release handles
fin.close()
fout.close()
