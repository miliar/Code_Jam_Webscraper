def isqrt(n):
	x1, x2 = 1, n
	while abs(x1 - x2) > 1:
		x1, x2 = x2, (x2 + n // x2) // 2
	return min(x1, x2)

def main():
	input = open("input.txt", "r")
	output = open("output.txt", "w")

	# Read the number of tests.
	tests = int(input.readline())

	print("There are " + str(tests) + " tests.")

	# Iterate over the tests.
	for i in range(1, tests + 1):
		data = input.readline().split(" ")
		min = int(data[0])
		max = int(data[1])
		
		# Square root both bounds.
		sqrt_min = isqrt(min)
		sqrt_max = isqrt(max)
		
		print("- Testing range " + str(min) + "-" + str(max))
		
		# Count the fair and squares.
		num_fas = 0
		for j in range(sqrt_min, sqrt_max + 1):
			# If the number falls outside the actual bound, remove it.
			num = j * j
			if num < min or max < num:
				continue
			
			# Check if the current number is a palindrome, otherwise it can't be fas.
			sj = str(j)
			if sj != sj[::-1]:
				continue
			
			# Square it and check again.
			sj = str(num)
			if sj != sj[::-1]:
				continue
			
			# It's fair and square so count it.
			print("-- " + sj + " is fair and square.")
			num_fas = num_fas + 1
		
		# Output the test case result.
		output.write("Case #" + str(i) + ": " + str(num_fas) + "\r\n")

# Call the main function.
main()