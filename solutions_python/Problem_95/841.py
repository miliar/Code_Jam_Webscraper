#!/bin/python

import fileinput

sampleOut = "qa zoo our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"
sampleIn = "zy qee ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"

trans = str.maketrans(sampleIn, sampleOut)

lines = fileinput.input(files=['tongues.in'])
N = int(lines[0])
for index in range(1, N + 1):
  line = lines[index].rstrip()
  out = line.translate(trans)
  print('Case #%d: %s' % (index, out))
lines.close()
