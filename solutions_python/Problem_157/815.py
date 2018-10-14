import sys
qmat = {("i", "j"): "k", ("i", "k"): "-j",
		("j", "i"): "-k", ("j", "k"): "i",
		("k", "i"): "j", ("k", "j"): "-i"}

sys.setrecursionlimit(100000)

storage = {}
reductions = {}

def multiply(a, b):	
	if a == "1":
		return b
	if b == "1":
		return a
	if a == "-1":
		return negate(b)
	if b == "-1":
		return negate(a)
	if a == b:
		return "-1"
	if ("-" in a) and ("-" in b):
		return multiply(a[1:], b[1:])
	if "-" in a:
		return multiply(b, a[1:])
	if "-" in b:
		return multiply(b[1:], a)
	return qmat[(a, b)]

def negate(a):
	if "-" in a:
		return a[1:]
	else:
		return "-" + a

def reduce(string):
	if len(string) < 2:
		return string
	if string in reductions:
		return reductions[string]
	a = string[0]
	b = string[1]
	mul = multiply(a, b)
	if "-" in mul:
		ans = negate(reduce(mul[1:] + string[2:]))
	else:
		ans = reduce(mul + string[2:])
		reductions[string] = ans
	return ans


def check_reducible_mem(string, items):
	key = (string, items)
	if key in storage:
		return storage[key]
	if len(items) == 0:
		ans = (len(string) == 0)
	elif len(items) == 1:
		reduced = reduce(string)
		ans = (reduced == items)
	elif len(items) == len(string):
		ans = (items == string)
	elif len(string) < len(items):
		ans = False
	elif reduce(string) != reduce(items):
		ans = False
	else:
		first = items[0]
		rest = items[1:]
		for i in range(1, len(string) + 1):
			sub = string[:i]
			strrest = string[i:]
			if check_reducible_mem(sub, first) and check_reducible_mem(strrest, rest):
				ans = True
				break
		else:
			ans = False
	storage[key] = ans
	return ans

def gcd(a, b):
	#assumption: b >= 0
	if(b > a):
		return gcd(b, a)
	if b == 0:
		return a
	elif b == 1:
		return 1
	return gcd(b, a % b)

def lcm(a, b):
	return a * b // gcd(a, b)

def check(original, L, X):
	# limit = min(lcm(L, 3), X)
	# for i in range(limit,0,-1):
	# 	if (X - i) % 4 == 0:
	# 		if check_reducible_mem(original * i, "ijk"):
	# 			return True
	# return False
	return check_reducible_mem(original * X, "ijk")

def format_ans(num, ans):
	print "Case #" + str(num) + ": " + str(ans)

rounds = int(raw_input())

for i in range(1, rounds + 1):
	L, X = map(int, raw_input().split())
	line = raw_input()
	if check(line, L, X):
		format_ans(i, "YES")
	else:
		format_ans(i, "NO")
