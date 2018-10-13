#!/usr/bin/python2.6
import sys
filez = open(sys.argv[1], 'r')
mapping = {'\n': '\n', ' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd':
's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l':
'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w':
'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q', 'q': 'z'}

n_lines = int(filez.readline())
for i in range(0, n_lines):
  print 'Case #%d:' % (i + 1),
  text = filez.readline()
  string = ''
  for j in range(0, len(text)):
    string += mapping[text[j]]
  print string.strip()
