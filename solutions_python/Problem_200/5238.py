a = []
t = int(input())
for _ in range(t):
	n = int(input())
	while True:
		s = str(n)
		count = 1;
		for i in range(len(s)-1):
			if s[i] <= s[i+1]:
				count += 1
		if count == len(s):
			a.append(n)
			break
		n -= 1

for i in range(1,len(a)+1,1):
	s = 'Case #'+str(i)+': '+str(a[i-1])
	print(s)