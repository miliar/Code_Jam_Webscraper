from sys import stdin

line = stdin.readline().split()
L = int(line[0])
D = int(line[1])
N = int(line[2])
words = []
transmits = []

for i in xrange(D):
	words.append(stdin.readline().strip())

for i in xrange(N):
	transmits.append(stdin.readline().strip())

filename = "alien_language.out"
FILE = open(filename,"w")

case = 1
for t in transmits:
	i = 0
	n = 0
	T = []
	while i < len(t):
		chr = t[i]
		if chr == "(":
			i += 1
			token = ""
			while t[i] != ")":
				token += t[i]
				i += 1
			T.append(token)
		else:
			T.append(t[i])
		i += 1
	
	for word in words:
		i = 0
		for i in xrange(len(word)):
			yeeha = True
			if not word[i] in T[i]:
				yeeha = False
				break
			i += 1
		if yeeha:
			n += 1
	
	line = "Case #" + str(case) + ": " + str(n)
	print line
	FILE.write(line + "\n")
	case += 1
	
			
FILE.close()
