import sys, re

l, d, n = map(int,raw_input().split())
words = set()

for i in xrange(d):
    words.add(raw_input())

for i in xrange(n):
    r = re.compile(raw_input().replace("(","[").replace(")","]"))
    print "Case #%d: %d" % ( i+1, len(filter(r.match, words)))
