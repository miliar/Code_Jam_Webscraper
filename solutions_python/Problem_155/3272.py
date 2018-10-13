def solve(cipher):
	cipher = cipher.split(' ')
	num_standing, str_index, s_max, zeros = 0, 0, int(cipher[0]), 0
	cipher = cipher[1]

	while (str_index < len(cipher)):
		if (str_index > num_standing + zeros):
			zeros += 1
		num_standing += int(cipher[str_index])
		str_index += 1
	return zeros

if __name__ == "__main__":
	testcases = input()

	for case in xrange(1, testcases+1):
		cipher = raw_input()
		print("Case #%i: %s" % (case, solve(cipher)))


	

