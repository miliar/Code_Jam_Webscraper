#!/usr/bin/python

translator = {
	'a' : 'y',
	'o' : 'e',
	'z' : 'q',
	'q' : 'z'
	}

samples = [
	"ejp mysljylc kd kxveddknmc re jsicpdrysi",
	"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
	"de kr kd eoya kw aej tysr re ujdr lkgc jv"
	]

outputs = [
	"our language is impossible to understand",
	"there are twenty six factorial possibilities",
	"so it is okay if you want to just give up"
	]

def learn(samples, outputs, translator):
	for sample, output in zip(samples, outputs):
		for c1, c2 in zip(sample, output):
			translator[c1] = c2

def translate(line, translator):
	return "".join([translator[c] for c in line])

learn(samples, outputs, translator)

import sys

sys.stdin.readline()
for num, sample in enumerate(sys.stdin.readlines(), 1):
	print("Case #%d: %s" % (num, translate(sample[:-1], translator)))

