#!/usr/bin/python

from sys import stdin

alphabet = {'y': 'a', 'e': 'o', 'q': 'z', 'z': 'q'}

input_pairs = ( ("ejp mysljylc kd kxveddknmc re jsicpdrysi","our language is impossible to understand"),("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","there are twenty six factorial possibilities"),("de kr kd eoya kw aej tysr re ujdr lkgc jv","so it is okay if you want to just give up"))

for pairs in (input_pairs):
    encoded = pairs[0]
    decoded = pairs[1]
    for letter_pos in range(len(encoded)-1):
        alphabet[encoded[letter_pos]] = decoded[letter_pos]


lines = stdin.readline()
for line_no in range(int(lines)):
    line = stdin.readline()
    decoded_line = ''
    for letter_pos in range(len(line)-1):
        decoded_line += alphabet[line[letter_pos]]
    print "Case #"+str(line_no+1)+": "+decoded_line
