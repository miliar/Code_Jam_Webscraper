test = int(input())

def flip(query):
	r = ''
	for x in query:
		if x == '+':
			r += '-'
		else:
			r += '+'
	return r
	
for t0 in range(test):
	print("Case #"+str(t0+1)+": ",end='')
	s,k = input().split(' ')
	k = int(k)
	count = 0
	for i in range(len(s)-k+1):
		if s[i] == '-':
			temp = s[:i]
			temp += flip(s[i:i+k])
			temp += s[i+k:]
			s = temp
			count+=1
	
	if '-' in s:
		print("IMPOSSIBLE")
	else:
		print(count)