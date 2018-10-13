#!/usr/bin/python

encoded = [
  "ejp mysljylc kd kxveddknmc re jsicpdrysi",
  "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
  "de kr kd eoya kw aej tysr re ujdr lkgc jv"
]

translated = [
  "our language is impossible to understand",
  "there are twenty six factorial possibilities",
  "so it is okay if you want to just give up"
]

table = dict()

for i in range(len(encoded)):
  for j, x in enumerate(encoded[i]):
    if 'a' <= x and x <= 'z':
      #table[translated[i][j]] = x
      table[x] = translated[i][j]

table['z'] = 'q'
table['q'] = 'z'

# for k in sorted(table.keys()):
#   print "{} -> {}".format(k, table[k])
#  
# print sorted(table.keys())
# print sorted(table.values())

#===============================================================================
# Process the input data
#===============================================================================

def translate(q):
  s = ""
  for x in q:
    if 'a' <= x and x <= 'z':
      s += table[x]
    else:
      s += x
  
  return s

from sys import stdin

T = int(stdin.readline())
for i in range(1, T+1):
  G = stdin.readline().strip()
  
  print "Case #{}: {}".format(i, translate(G))