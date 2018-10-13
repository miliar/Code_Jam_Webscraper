import sys
from string import maketrans

# Making traslate map
googlerese = 'ynficwlbkuomxsevzpdrjgthaq'
english = 'abcdefghijklmnopqrstuvwxyz'
transtable = maketrans(googlerese, english)

# Reading input file
file = open(sys.argv[1], 'r')
testcases = int(file.readline())

output = []
for line in file:
	line = line.strip('\n')
	line = line.translate(transtable)
	output.append(line)

i = 1
while i <= testcases:
	print 'Case #%d: %s' % (i, output[i - 1])
	i = i + 1

file.close()