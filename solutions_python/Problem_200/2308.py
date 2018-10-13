def main():
	s = input()
	if len(s) < 2:
		return s
	a, b = 0, 1
	start = 0
	res = []
	while b < len(s):
		da, db = int(s[a]), int(s[b])
		if da == db:
			a += 1
			b += 1
		elif da < db:
			a += 1
			b += 1
			start = a
		elif da > db:
			if da == 1:
				return "9" * (len(s) - 1)
			else:
				res = res[:start]
				res.append(da - 1)
				while len(res) < len(s):
					res.append(9)
				return ''.join(map(lambda i : str(i), res))
		res.append(da)
	return s

				
line = int(input())
res = ''
for i in range(line):
	res += "Case #" + str(i + 1) + ": " + main() + "\n"
print(res)