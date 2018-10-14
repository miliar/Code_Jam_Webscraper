#!/usr/bin/python

import sys
import re

learn = open('a.learn').read()
learn2 = open('a.learn2').read()

decode = {}

for i in range(len(learn)):
    if learn[i] in decode:
        if decode[learn[i]] != learn2[i]:
            print "erreur"
    elif learn[i] >= 'a' and learn[i] <= 'z':
        decode[learn[i]] = learn2[i]

data = open('asmall.in')
data.readline()
i = 1
for line in data:
    sys.stdout.write("Case #" + str(i) + ": ")
    i += 1
    for j in range(len(line)):
        if line[j] in decode:
            sys.stdout.write(decode[line[j]])
        else:
            sys.stdout.write(line[j])

