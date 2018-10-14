t = int(raw_input())

def invert(ch):
	if ch == '+':
		return '-'
	else:
		return '+'


for c in range(t):
	s, k = raw_input().split(' ')
	k = int(k)
	s = map(lambda x: x, s)

	#print s, k

	changes = 0

	ans = ""

	for j in range(len(s)):
		if s[j] == '-':
			if len(s) - j >= k:
				changes += 1
				for l in range(k):
					s[j + l] = invert(s[j + l])	
			else:
				ans = "IMPOSSIBLE"

	if ans == "":
		ans = str(changes)

	print "Case #{0}: {1}".format(c+1, ans) 


