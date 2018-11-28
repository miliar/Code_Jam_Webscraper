def minTidy(n):
	n = list(n)
	rf = [1]
	sol = n
	lastInc = 0
	firstDec = -1
	for i in range(1, len(n)):
		if n[i] > n[i-1]:
			lastInc = i
		elif n[i] < n[i-1]:
			firstDec = i
			break
	if firstDec == -1:
		return "".join(n)
	n[lastInc] = chr(ord(n[lastInc])-1)
	for i in range(lastInc+1,len(n)):
		n[i] = '9'
	if n[0] == '0':
		n = n[1:]
	return "".join(n)
