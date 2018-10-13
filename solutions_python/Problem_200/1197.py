fin = open("testb.in")
fout = open("testb.out", "w")

def is_tidy(n):
	return sorted(list(n)) == list(n)

def solve():
	n = fin.readline().rstrip()
	if is_tidy(n):
		return n

	for i in range(len(n) - 1, -1, -1):
		if (n[i] == '0'):
			continue
		ans = n[:i] + str(int(n[i]) - 1) + '9' * (len(n) - i - 1)
		if is_tidy(ans):
			return str(int(ans))


for test_num in range(1, int(fin.readline()) + 1):
	print("Case #" + str(test_num) + ": " + solve(), file = fout)
fout.close()