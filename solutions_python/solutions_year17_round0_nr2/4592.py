def last_tidy_num(num):
	for i in range(num, 0, -1):
		str_i = str(i)
		if list(str_i)==sorted(str_i):
			return i

T = int(input())

for T0 in range(T):
	N = int(input())
	num = last_tidy_num(N)
	print("Case #{}: {}".format(T0+1, num))

