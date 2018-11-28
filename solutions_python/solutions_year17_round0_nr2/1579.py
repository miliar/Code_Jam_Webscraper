import sys

# WARNING: Assumes all input is squeaky clean.

def main():
	T = int(sys.stdin.readline())

	for case_num in range(1,T+1):
		input_line = sys.stdin.readline()
		N = int(input_line)

		y = find_tidy_predecessor(N)

		print("Case #{0}: {1}".format(case_num, y))

def find_tidy_predecessor(N):
	y = N
	mag = 1
	while mag < y:
		last_digit = (y % (mag*10))/mag
		mag *= 10
		current_digit = (y % (mag*10))/mag
		if current_digit > last_digit:
			y -= (y % mag)+1
	return y

def is_tidy(N):
	pot = 1
	last_digit = (N % (pot*10))/pot
	while pot < N:
		pot *= 10
		current_digit = (N % (pot*10))/pot
		print current_digit, last_digit
		if current_digit > last_digit:
			return False
		last_digit = current_digit
	return True

if __name__ == "__main__":
	main()