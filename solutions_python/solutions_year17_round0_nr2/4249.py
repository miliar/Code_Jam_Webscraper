t = int(input())

def isTidy(num):
	num = str(num)
	for i in range(len(num) - 1):
		if num[i] > num[i + 1]:
			return False

	return True

def split(num):
	while not isTidy(num):
		l = [int(i) for i in str(num)]
		for i in range(len(l) - 1, -1, -1):
			if (i == 0):
				l[i] -= 1
				break

			if l[i-1] <= l[i]:
				l[i] = 9
			else:
				l[i] = 9
				l[i-1] -= 1
				break

		# print(l)

		num = int("".join(map(str, l)))

	return num


for i in range(t):
	n = int(input())
	print("Case #{}:".format(i+1), split(n))
