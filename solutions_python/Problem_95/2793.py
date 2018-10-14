#!/usr/bin/python

from string import maketrans

language = "ynficwlbkuomxsevzpdrjgthaq"
google = "abcdefghijklmnopqrstuvwxyz"
table = maketrans(language, google)

f = open('random.txt', 'r')

tests = f.readline()

count = 1

while count <= int(tests):
	temp = str(f.readline())
	print "Case #" + str(count) + ":",
	print temp.translate(table),
	count += 1