#!/usr/bin/python2.5

import sys

PHRASE = "welcome to code jam"

def Find(text, phrase):
  if not phrase:
    return 1

  result = 0
  first_letter = phrase[0]
  for i, letter in enumerate(text):
    if not letter == first_letter:
      continue
    result += Find(text[i:], phrase[1:])

  return result


N = int(sys.stdin.readline())
texts = tuple(sys.stdin.readline().strip() for n in xrange(N))

for i, text in enumerate(texts):
  result = Find(text, PHRASE)
  print "Case #%d: %04d" % (i + 1, result)
