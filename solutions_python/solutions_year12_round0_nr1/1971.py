#! /usr/bin/env python

import sys
import string

filename = sys.argv[1]
file = open(filename, 'r')
lines = file.readlines()
S = int(lines.pop(0))  #pop off how many lines there are
file.close()
# E - T   English - Translation
# a - y
# b - n
# c - f
# d - i
# e - c
# f - w
# g - l
# h - b
# i - k
# j - u
# k - o
# l - m
# m - x
# n - s
# o - e
# p - v
# q - *z
# r - p
# s - d
# t - r
# u - j
# v - g
# w - t
# x - h
# y - a
# z - *q
# * mean that translation could not be seen in example executions
table = string.maketrans("ynficwlbkuomxsevzpdrjgthaq", string.ascii_lowercase)
for i in range(0, S):
  line = lines[i].strip()
  #print line
  print "Case #%d: %s" % (i + 1, line.translate(table))
  