#!/usr/bin/env python
import re
import sys

data = []
with open(sys.argv[1]) as file:
    data = file.readlines()

letterC, wordC, caseC = re.compile(r'^([0-9]*) ([0-9]*) ([0-9]*)$').findall(data[0])[0]

words = ""
cases = []

for row in data[1:int(wordC)+1]:
    words += row + " "

for row in data[int(wordC)+1:]:
    cases.append(row.replace("(", "[").replace(")", "]").strip())

counter = 1
txt = ""
for case in cases:
    txt += "Case #" + str(counter) + ": " + str(len(re.compile(case).findall(words))) + "\n"
    counter += 1

with open(sys.argv[1]+".res", "w") as file:
    file.write(txt)

