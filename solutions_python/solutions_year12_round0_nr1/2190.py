import sys

learn = open("learn.txt")

l1 = learn.readline()
l2 = learn.readline()
y = range(0,26)
x = ['-']*26
for i in range(0, len(l1)-1):
	if (l1[i] != ' ') :
		y[ord(l2[i])-ord('a')] = -1
		x[ord(l1[i])-ord('a')] = l2[i]

x[25] = 'q'
x[16] = 'z'

inp = open("input.in")

num = int(inp.readline())

for i in range(0, num) :
	line = inp.readline()
	out = ""
	for j in range(0, len(line)) :
		if (line[j] == ' '):
			out = out + ' '
		elif (line[j] != '\n'):
		 	out = out + x[ord(line[j]) - ord('a')]
	print "Case #" + str(i+1) + ": " + out
