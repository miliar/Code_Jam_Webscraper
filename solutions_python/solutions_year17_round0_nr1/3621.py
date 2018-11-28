n = int(input())
for i in range(n):
	str1 = input()
	str1 = str1.split(" ")
	inp = str1[0]
	k = int(str1[1])
	c = 0
	for j in range(len(inp)-(k-1)):
		if(inp[j] == '-'):
			c = c + 1
			for m in range(j,j+k):
				inp = list(inp)
				if(inp[m] == '-'):
					inp[m] = '+'
				else:
					inp[m] = '-'
				inp = ''.join(inp)
	if '-' in inp:
		print("Case #",i+1,": IMPOSSIBLE",sep="")
	else:
		print("Case #",i+1,": ",c,sep="")
