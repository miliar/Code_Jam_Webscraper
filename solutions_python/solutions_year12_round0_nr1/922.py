import math
f = open("testcase.txt")
c = int(f.readline())
diction = {"a": "y", "b": "h", "c": "e", "d": "s", "e": "o", "f": "c", "g": "v", "h": "x", "i": "d", "j": "u", "k": "i", "l": "g", "m": "l", "n": "b", "o": "k", "p": "r", "q": "z", "r": "t", "s": "n", "t": "w", "u": "j", "v": "p", "w": "f", "x": "m", "y": "a", "z": "q", " ": " "}
for l in xrange(c):
	d = f.readline().rstrip('\n')
	translated = ""
	for i in d:
		translated += diction[i]
	print "Case #"+str(l+1)+": "+translated
