n = int(input())



def isTidy(n):
	s = str(n)
	old = int(s[0])
	for i in range(1, len(s)):
		if int(s[i]) < old:
			return False
		old = int(s[i])

	return True


def Tidy(num):

	s = str(num)
	c = 1
	while not isTidy(num):
		for i in range(len(s) - 1, 0, -1):
			if int(s[i]) < int(s[i - 1]) or int(s[i]) == 0 or int(s[i - 1]) == 0:
				num -= 10**(len(s) - (i + 1))
				break

		s = str(num)

	return num

for i in range(n):
	num = int(input())
	print("Case #{}: {}".format(i+1, Tidy(num)))
