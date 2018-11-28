def tidy(N):

	# the first comparison is always legit
	curr = 10

	# loop until we're processed the whole number
	while N > 0:

		# get the current digit
		prev = curr
		N, curr = divmod(N, 10)

		# the number is non-ascending if a less significant digit is lower than a more significant one
		if prev < curr:
			return False

	# if we made it this far, that means the number didn't break the tidy rules
	return True


def max_tidy_brute(N):

	# count down from the max value
	for curr in reversed(range(1, N + 1)):

		# if the current number is increasing, we're good to go
		if tidy(curr):
			return curr

	# 1 is a tidy number
	return 1

MAX_ORDER = 9
def max_tidy(N):

	# keep modifying the number until it's tidy
	curr = N
	magnitude = 1
	next_magnitude = 10 * magnitude
	while not tidy(curr):

		# extract the current digit
		digit = (curr % next_magnitude) // magnitude

		# increase the current digit to its max order
		curr += magnitude * (MAX_ORDER - digit)

		# decrease the next digit by one order
		curr -= next_magnitude

		# incrase our magnitude
		magnitude = next_magnitude
		next_magnitude = 10 * magnitude

	return curr

# play each case
num_cases = int(input())
for case_num in range(num_cases):

	# read in the current case
	N = int(input())

	# run the current case
	print("Case #{case}: {result}".format(
		case=case_num + 1,
		result=max_tidy(N),
	))
