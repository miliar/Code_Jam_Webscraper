def checkDone(s):
	for i in s:
		if(i == '-'):
			return False
	return True

def flipLeft(s, k):
	for i in range(k):
		if(s[i] == '-'):
			s = list(s)
			s[i] = '+'
			s = ''.join(s)
		else:
			s = list(s)
			s[i] = '-'
			s = ''.join(s)
	return s

def flipRight(s, k):
	for i in range(k):
		if(s[len(s)-1-i] == '-'):
			s = list(s)
			s[len(s)-1-i] = '+'
			s = ''.join(s)
		else:
			s = list(s)
			s[len(s)-1-i] = '-'
			s = ''.join(s)
	return s

def solve(s, k):
	count = 0
	if checkDone(s):
		return count
	s = s.strip('+')
	if(len(s) < k):
		return -1
	while True:
		s = flipLeft(s, k)
		count += 1
		s = s.strip('+')
		if checkDone(s):
			return count
		if(len(s) < k):
			return -1
		s = flipRight(s, k)
		count += 1
		s = s.strip('+')
		if checkDone(s):
			return count
		if(len(s) < k):
			return -1
	return -1


T = int(input())
for i in range(T):
	line = input().split()
	s = line[0]
	k = int(line[1])
	answer = solve(s, k)
	if(answer < 0):
		print("Case #%d: IMPOSSIBLE" % (i+1))
	else:
		print("Case #%d: %d" % (i+1, answer))
		



