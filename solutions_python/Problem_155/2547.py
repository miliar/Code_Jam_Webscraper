

def problema():
	T = int(input())

	for i in range(T):
		case = input().split()
		case[0] = int(case[0])

		print("Case #%s: %s" % (i+1, compute(case[0], case[1])))


def compute(smax, strk):
	current_standing = 0
	needed = 0
	for i, c in enumerate(strk):
		c = int(c)
		if c > 0:
			current_standing += c
		else:
			if current_standing <= i:
				j = i - current_standing +1
				needed += j
				current_standing += j
			else:
				current_standing += c


	return needed



if __name__ == "__main__":
	problema()