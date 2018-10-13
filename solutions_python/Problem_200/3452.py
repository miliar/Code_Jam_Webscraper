def getwrongindex(n):
	for i in range(len(n)-1):
		if n[i] > n[i+1]:
			return i
	return len(n)
def decrementdigit(c):
	return chr(ord(c)-1)
def getlasttidy(n):
	l = list(n)
	length = len(l)
	if length == 1:
		return n
	k = getwrongindex(n)
	if k == length:
		return n
	i = k
	while i>=0:
		newdigit = decrementdigit(n[i])
		if i == 0  or (n[i] != n[i-1] and newdigit != '0'):
			l[i] = newdigit
			break
		l[i] = '9' 
		i -= 1
	for j in range(k+1,length):
		l[j] = '9'
	return ''.join(l).lstrip('0')

t = int(input())

for a0 in range(t):
	n = input()
	ans = getlasttidy(n)
	print("Case #{}: {}".format(a0+1,ans))