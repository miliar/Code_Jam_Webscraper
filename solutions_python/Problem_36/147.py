import urllib2
import sys
import re

def check_pattern_it( word, pattern):
	res = []
	for j in range(0, len(pattern)):
		previous = 0
		cur = 0
		res.append([])
		for i in range(0, len(word)):
			if j == 0:
				cur = previous
				if word[i] == pattern[j]:
					cur += 1
			else:
				cur = previous
				if word[i] == pattern[j] and i != 0:
					cur += res[j-1][i-1]
				cur = cur % 10000
			previous = cur
			res[j].append(cur)
	return res[len(pattern) - 1][len(word) - 1]

	
file = open(sys.argv[1], 'r')

fline = file.readline()
nbLine = int(fline)

j = 1
for i in range(0, nbLine):
	res = check_pattern_it(file.readline(), 'welcome to code jam')
	print "Case #%d: %04d" % (j, res % 10000)
	j += 1
	