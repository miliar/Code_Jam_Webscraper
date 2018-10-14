#!/usr/bin/python
from string import maketrans
from string import translate
table = maketrans("abcdefghijklmnopqrstuvwxyz","yhesocvxduiglbkrztnwjpfmaq")
cases = int(raw_input())
for i in xrange(cases):
    a = raw_input()
    print "Case #%d: %s" % (i+1,translate(a,table))
