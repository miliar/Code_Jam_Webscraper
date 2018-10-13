#!/usr/bin/env python

import fileinput

def calculate(queries, size):
  count = 0  # no switches so far
  options = set(range(size))  # what we *could* be using
  for query in queries:
    options.discard(query)
    if not options:
      # we decide in retrospect that we were using this search engine
      # since the last change
      # we don't know what we will change to here,
      # but we know it is not this one
      options = set(range(size)).difference([query])
      count += 1
  return count  

f = fileinput.input()
for i in range(1, 1 + int(f.readline())):
  search_engines = [f.readline()[:-1] for _ in range(int(f.readline()))]
  queries = [search_engines.index(f.readline()[:-1]) for _ in range(int(f.readline()))]
  print "Case #%d: %d" % (i, calculate(queries, len(search_engines)))
