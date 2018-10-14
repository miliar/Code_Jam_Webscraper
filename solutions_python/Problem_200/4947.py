n = int(input())


def isTidy(n):
	s = str(n)
	old = int(s[0])
	for i in range(1, len(s)):
		if int(s[i]) < old:
			return False
		else:
			old = int(s[i])

	return True

for i in range(n):
	num = int(input())
	while not isTidy(num):
		num -= 1
	print("Case #{}: {}".format(i+1, num))
