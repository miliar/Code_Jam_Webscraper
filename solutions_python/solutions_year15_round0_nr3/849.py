def multiply(part, count):
	if part[-1] == '\n':
		part = part[:-1]
	expr = list(part * count)
	expr.reverse()
	sign = '+'
	res = ""
	base = ['i', 'j', 'k']
	wanted = 0
	while len(expr) > 1:
		if wanted < len(base) and expr[-1] == base[wanted]:
			res += expr.pop()
			wanted += 1
		else:
			sign, buf = mul(sign, expr.pop(), expr.pop())
			expr.append(buf)
	if wanted < len(base) and expr[0] == base[wanted]:
		res += expr.pop()
	if res == "ijk" and sign == '+' and (len(expr) == 0 or expr[0] == '1'):
		return "YES"
	else:
		return "NO"


def mul(sign, a, b):
	minus = False
	ans = ""

	if a == '1':
		ans = b
	elif b == '1':
		ans = a
	elif a == b:
		minus = True
		ans = '1'
	elif a == 'i' and b == 'j':
		ans = 'k'
	elif a == 'i' and b == 'k':
		minus = True
		ans = 'j'
	elif a == 'j' and b == 'i':
		minus = True
		ans = 'k'
	elif a == 'j' and b == 'k':
		ans = 'i'
	elif a == 'k' and b == 'i':
		ans = 'j'
	elif a == 'k' and b == 'j':
		minus = True
		ans = "i"

	if (sign == '-' and minus) or (sign == '+' and not minus):
		return ['+', ans]
	else:
		return ['-', ans]

inp = open("test.in", 'r')
t = int(inp.readline())
i = 1
res = open("res.txt", 'w')
while i <= t:
	times = int(inp.readline().split()[1])
	symbols = inp.readline()
	res.writelines("Case #" + str(i) + ": " + str(multiply(symbols, times)) + "\n")
	i += 1
res.close()
inp.close()