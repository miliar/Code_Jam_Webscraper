def main():
	inp, n = input().split()
	n = int(n)
	inp = list(inp)
	if len(inp) < n:
		for c in inp:
			if c == '-':
				return "IMPOSSIBLE"
		return "0"
	res = 0
	for i in range(len(inp)):
		if i + n <= len(inp) and inp[i] == "-":
			valid = True
			for j in range(n):
				if inp[i + j] == "+":
					inp[i + j] = "-"
					valid = False
				elif inp[i + j] == "-":
					inp[i + j] = "+"
			res += 1
			if i + n == len(inp) and valid == True:
				return str(res)
	for ch in inp:
		if ch == '-':
			return "IMPOSSIBLE"
	return str(res)

				
line = int(input())
res = ''
for i in range(line):
	res += "Case #" + str(i + 1) + ": " + main() + "\n"
print(res)

