#!/usr/bin/python

from string import *

n = (int)(raw_input())
for i in range(n):
    s = raw_input()
    print "Case #%d: %s" % (i+1, s.translate(maketrans(" zqacbedgfihkjmlonpsrutwvyx", " qzyehosvcdxiulgkbrntjwfpam"), ""))
