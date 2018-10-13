fin = open("testa.in")
fout = open("testa.out", "w")

def solve():
	s, k = fin.readline().rstrip().split()
	s = [int(s[i] != '-') for i in range(len(s))]
	k = int(k)
	ans = 0
	for i in range(len(s) - k + 1):
		if s[i] == 0:
			ans += 1
			for j in range(i, i + k):
				s[j] = 1 - s[j]
	if sum(s) != len(s):
		return "IMPOSSIBLE"
	return str(ans)


for test_num in range(1, int(fin.readline().rstrip()) + 1):
	print("Case #" + str(test_num) + ": " + solve(), file = fout)
fout.close()