#!/usr/bin/python
kk = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}
store = []
trans = []
times = int(raw_input())
for each in range(times):
	store.append(raw_input())

for sentance in store:
	translation = ""
	for letter in sentance:
		translation += kk[letter]
	trans.append(translation)
i = 1
for sentance in trans:
	print "Case #" + str(i) + ": " + sentance
	i += 1
