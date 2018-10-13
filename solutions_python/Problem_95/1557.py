#!/usr/bin/python

masterDict = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

fd = open('input.txt','r')
count = int(fd.readline().strip())
iterator = 0
while iterator < count:
    iterator += 1
    input = fd.readline().strip()
    output = "Case #%s: " % iterator
    for x in input:
        output = output + masterDict[x]
    print output
