#!/usr/bin/env python

cache = {}
def count(string, pattern):
  if len(pattern) > len(string):
    # No match if pattern is longer than search string
    return 0

  # Check cache if search string is longer than 20 chars
  if len(string) > 20:
    if cache.has_key((string,pattern)):
      return cache[(string,pattern)]

  result = 0
  for i in range(0, len(string) - len(pattern) + 1):
    if string[i] == pattern[0]:
      if len(pattern) == 1:
        result += 1
      else:
        result += count(string[i + 1:], pattern[1:])
  if len(string) > 20:
    cache[(string,pattern)] = result
  return result

input = open("C-large.in", "r")
lines = input.readlines()

for i in range(1, len(lines)):
  result = count(lines[i], "welcome to code jam")
  resultstr = ('%04d' % result)[-4:]
  print 'Case #%i: %s' % (i, resultstr)

