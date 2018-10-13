T = int(raw_input())

def flip(c):
	return "+" if c == "-" else "-"

def get_flips(s,k):
	flips = 0
	for i in range(len(s)):
		if s[i] == '+':
			continue
		elif i+k > len(s):
			return "IMPOSSIBLE"
		else:
			for j in range(i, i+k):
				s[j] = flip(s[j])
			flips += 1
	return flips

for test_case in range(T):
	S, K = raw_input().split()
	flips = get_flips(list(S), int(K))
	print "Case #%s: %s"%(test_case+1, flips)
