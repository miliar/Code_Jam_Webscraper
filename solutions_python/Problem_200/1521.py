

if __name__ == "__main__":
	# read the input
	case_count = int(raw_input())
	for case in range(case_count):
		s = raw_input()
		length = len(s)
		digits = map(lambda c: ord(c) - 48, s)
		#
		#
		#
		# find the first descending, and the last ascending before it
		first_descending = -1
		last_ascending   = -1
		for i in range(length-1):
			if digits[i] > digits[i+1]:
				first_descending = i
				break
		for i in range(first_descending):
			if digits[i] < digits[i+1]:
				last_ascending = i
		#
		#
		#
		if first_descending == -1:
			# situation #1: never descend
			ans = s
		elif last_ascending == -1:
			# situation #2: had descend but never ascend
			if digits[0] == 1:
				ans = "9" * (length - 1)
			else:
				ans = str(digits[0]-1) + "9" * (length - 1)
		else:
			# situation #3: had ascend before the first descend
			ans = s[:(last_ascending + 1)] + str(digits[last_ascending + 1] - 1) + "9" * (length - last_ascending - 2)
		#
		#
		#
		print "Case #%d: %s" % (case + 1, ans)
