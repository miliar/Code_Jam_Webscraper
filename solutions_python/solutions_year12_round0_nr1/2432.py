#!/usr/bin/env python2

transform = {"y": "a", "n": "b", "f": "c", "i": "d", "c": "e", "w": "f", "l": "g", "b": "h", "k": "i", "u": "j", "o": "k", "m": "l", "x": "m", "s": "n", "e": "o", "v": "p", "z": "q", "p": "r", "d": "s", "r": "t", "j": "u", "g": "v", "t": "w", "h": "x", "a": "y", "q": "z", " ": " "}

count = int(raw_input())
for x in xrange(0,count):
  in_word = list(raw_input())
  out_list = []
  for y in xrange(0,len(in_word)):
    out_list.append(transform[in_word[y]])
  out_word = ''.join(out_list)
  print "Case #" + str(x+1) + ": " + out_word