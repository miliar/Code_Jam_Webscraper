import sys
import os
import re
import string

pattern = re.compile('')

N = input()

def check(line):
  chars = list('0123456789abcdefghijklmnopqrstuvwxyz')
  origin = []
  choice = []
  first = line[0]
  length = max(2, len(set(line)))
  for i, c in enumerate(line):
    if not c in origin:
      origin.append(c)
      if c==first:
        choice.append(chars.pop(1))
      else:
        choice.append(chars.pop(0))
  tbl = string.maketrans(''.join(origin), ''.join(choice))
  reg = line.translate(tbl)
  #print reg, length
  return int(reg, length)

for i in range(N):
  line = raw_input()
  print 'Case #%d:' % (i+1), check(line)

