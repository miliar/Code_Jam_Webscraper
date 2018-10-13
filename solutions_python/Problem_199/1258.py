t = int(input())

def flip(s, k):
	s = list(s)
	i = 0
	f = 0
	while i <= len(s)-k:
		if s[i]=="-":
			f += 1
			for j in range(i, i+k):
				s[j] = ("+" if s[j]=="-" else "-")
		i += 1

	return (f if len(set(s))==1 else "IMPOSSIBLE")

for i in range(t):
	s,k = input().split(" ")
	res = flip(s, int(k))
	print("Case #{}: {}".format(i+1, res))