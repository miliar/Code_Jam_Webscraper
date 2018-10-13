#!/usr/bin/python2
from sys import stdin

inp = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
out = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"

trans = [0 for i in range(26)]
trans[ord('z') - ord('a')] = 'q'
trans[ord('q') - ord('a')] = 'z'

for n, i in enumerate(inp):
  if i != " ":
    trans[ord(i) - ord('a')] = out[n]

#print trans

def tr(s):
  ret = ""
  for c in s:
    if c != " ":
      ret += trans[ord(c) - ord('a')]
    else:
      ret += c
  return ret

C = int(stdin.readline())
for c in range(1,C+1):
  t = stdin.readline()[:-1]
  #print "'" + t + "'"
  print "Case #%d: %s" %(c, tr(t))
