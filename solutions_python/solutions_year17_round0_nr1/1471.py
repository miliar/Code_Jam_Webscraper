inp =  open("A.in", "r")
T = int(inp.readline())
cases = []
for line in inp:
	s , k = line.split(" ")
	cases.append((s, int(k)))
inp.close()

out =  open("A.out", "wb") 


for cs in range(T):
	s , k = cases[cs]
	ans = 0
	size = len(s)
	for i in range(size):
		if s[i] == '-':
			if i + k - 1 < size:
				ans += 1
				for j in range(i, i+k):
					c = '+' if (s[j] == '-') else '-'
					s = s[:j] + c + s[j + 1:]
			else:
				ans = -1
				break

	if ans != -1:
		out.write("Case #%d: %d\n" % (cs+1, ans))
	else:
		out.write("Case #%d: IMPOSSIBLE\n" % (cs+1))
			

out.close()
