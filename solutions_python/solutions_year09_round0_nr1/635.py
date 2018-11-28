from string import strip, find
import re

#lines = open('lol.in','r').readlines()
lines = open('a_input.in','r').readlines()

known = []
shazan = []
i = 1

def howMany(word):
	ret = 0
	for i in known:
		if i == word: ret = ret+1
	return ret	

for line in lines:
	if i is 1:
		l, d, n = line.split()
		#print l, d, n
	elif i <= int(d)+1:
		known.append(line.strip('\n'))
	else:
		shazan.append(line.strip('\n'))
	i = i+1

#print known
#print shazan
cases = []
for word in shazan:
	x = word.find('(')
	if x == -1:
		cases.append(howMany(word))
		continue

	thePattern = "^"+word.replace("(","[").replace(")","]")+"$"
	matches = [re.match(thePattern,h) for h in known if re.match(thePattern,h) is not None]
	cases.append(len(matches))
	
for i in range(len(cases)):
	print "Case #%d: %d" % (i+1, cases[i])
