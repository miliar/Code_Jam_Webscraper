def find_untidiness(N):
	# A tidy number is one such that N[i-1] > N[i] is never true
	for i in range(1,len(N)):
		if N[i-1] > N[i]:
			return i

	return -1


for t in range(int(input())):
	case_t = input()

	digit_list = [int(x) for x in list(case_t)]
	digits_n = len(digit_list)

	ans = "not found"

	while True:
		# find the first conflict from the left
		i = find_untidiness(digit_list)

		if i == -1:
			ans = "".join(str(x) for x in digit_list)
			break

		# digit_list[i-1] > digit_list[i]
		digit_list[i-1] = digit_list[i-1] - 1
		digit_list[i] = int('9'*(digits_n-i))
		digit_list = digit_list[0:i+1]

		# we don't like left zeros
		if digit_list[0] == 0: 
			del digit_list[0]

	print("Case #{0}: {1}".format(t+1, ans))