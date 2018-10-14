

if __name__ == "__main__":
	case_count = int(raw_input())
	for case in range(case_count):
		tokens = raw_input().strip().split()
		sequence = map(lambda e: False if e == "-" else True, tokens[0])
		k = int(tokens[1])
		ans = 0
		for i in range(len(sequence) - (k-1)):
			if sequence[i] == False:
				# flip
				sequence[i : i+k] = map(lambda e: (not e), sequence[i : i+k])
				ans += 1

		# check
		for i in range(len(sequence)):
			if sequence[i] == False:
				ans = -1
				break


		if ans == -1:
			print "Case #%d: IMPOSSIBLE" % (case + 1)
		else:
			print "Case #%d: %d" % (case + 1, ans)