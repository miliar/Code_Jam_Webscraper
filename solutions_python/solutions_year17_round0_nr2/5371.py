

def is_tidy(number):
	number = list(str(number))
	for i in range(0, len(number)-1):
		if number[i] > number[i+1]:
			return False
	return True


def solve(lnumber):
	temp_tidy = lnumber
	for number in range(1,lnumber+1):
		if is_tidy(number):
			temp_tidy = number

	return temp_tidy


if __name__ == "__main__":

	t = int(input())  # read a line with a single integer
	for i in range(1, t + 1):
		last_number = input()
		answer = solve(int(last_number))
		print("Case #{}: {}".format(i, answer))
		# check out .format's specification for more formatting options