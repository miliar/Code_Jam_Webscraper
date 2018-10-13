import sys

def flip(s, k):
	s = list(s)
	l = len(s)
	count = 0
	for i in range(0,l-k+1):
		if (s[i] == '-') :
			count = count+1
			for j in range(0,k):
				if (s[i+j] == '-'):
					s[i+j] = '+'
				else:
					s[i+j] = '-'
	for i in range(0,l):
		if (s[i] == '-'):
			return -1
	return count

t = input()
for i in range(0, t):
	case = raw_input()
	s = case.split(" ")
	k = int(s[1])
	s = s[0]
	res = flip(s,k)
	if res == -1:
		print "Case #"+`i+1`+": IMPOSSIBLE"
	else:
		print "Case #"+`i+1`+": "+`res`
