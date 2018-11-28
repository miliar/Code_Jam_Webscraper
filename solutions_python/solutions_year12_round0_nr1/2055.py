#!/usr/bin/python

a = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
b = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"

map = {}

for i in range(len(a)):
  map[a[i]] = b[i]

map['z'] = 'q'
map['q'] = 'z'


def solve():
  s = raw_input()
  a = []
  for i in range(len(s)):
    a.append(map[s[i]])

  return ''.join(a)

for i in xrange(input()):
  print "Case #%d: %s" % (i+1, solve())



