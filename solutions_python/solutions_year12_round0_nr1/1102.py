#!/usr/bin/env python
# encoding: utf-8

google = ['ejp mysljylc kd kxveddknmc re jsicpdrysi',
          'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
          'de kr kd eoya kw aej tysr re ujdr lkgc jv']

nature = ['our language is impossible to understand',
          'there are twenty six factorial possibilities',
          'so it is okay if you want to just give up']

alphabet = 'abcdefghijklmnopqrstuvwxyz'
mapping = {}
for letter in alphabet:
    mapping[letter] = []

for i in range(len(google)):
    for j in range(len(google[i])):
        if google[i][j] == ' ':
            continue
        mapping[google[i][j]].append( nature[i][j] )

for k in mapping:
    mapping[k] = list(set(mapping[k]))

mapping = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'q': 'z', 'z': 'q'}

def char_convert(line):
    ret = ''
    for c in line:
        if c.isspace():
            ret += c
        else:
            ret += mapping[c]
    return ret

result = []
T = 0
i = 0
fd = open('A-small-attempt0.in')
for line in fd:
    if line.rstrip('\n').isdigit():
        T = int(line)
    else:
        i += 1
        result.append( 'Case #' + str(i) + ': ' + char_convert(line) )
        if i >= T:
            break
fd.close()

fd = open('b.txt', 'w')
fd.writelines(result)
fd.close()
