t = int(input())
for index in range(t):
	s,k = input().split()
	s = list(s)
	k = int(k)
	nb = 0
	for i in range(len(s)-k+1):
		if s[i]=="-":
			nb += 1
			s[i] = "+"
			for j in range(1,k):
				s[i+j] = "+" if s[i+j]=="-" else "-"
	possible = True
	for j in range(len(s)-k+1,len(s)):
		if s[j] == "-":
			possible = False
	if possible:
		print("Case #"+str(index+1)+": "+str(nb))
	else:
		print("Case #"+str(index+1)+": IMPOSSIBLE")
