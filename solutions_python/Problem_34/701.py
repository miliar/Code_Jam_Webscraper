from sys import argv
import re

fin = open(argv[1])
input = fin.readlines()

temp = input[0].split()
l = int(temp[0])
d = int(temp[1])
n = int(temp[2])

#list of words
words = []
for i in xrange(1,d+1):
    words.append(input[i].strip())  #Since ending in "\n" so strip

#list of patterns
patterns = []
for i in xrange(d+1,d+n+1):
    temp = input[i].strip()
    temp = temp.replace('(','[')
    temp = temp.replace(')',']')
    patterns.append(temp)

for i in xrange(n):
    count = 0
    for j in words:
        if re.match(patterns[i], j):
            count += 1
    print "Case #%d: %d" % (i+1, count)

    