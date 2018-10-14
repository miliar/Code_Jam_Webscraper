data= {'q': 'z', 'z': 'q', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm'}
n = int(raw_input())
for i in range(n):
	line = raw_input()
	ans=''
	for j in line:
		if j==' ':
			ans+=' '
		else:
			ans+=data[j]
	print 'Case #'+str(i+1)+': '+ans

