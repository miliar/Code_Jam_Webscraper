tc = int(raw_input())
for case_no in range(1, tc+1):
	a, b, k = map(int, raw_input().split())
	answer = 0
	for a_val in range(a):
		for b_val in range(b):
			if a_val & b_val < k:
				answer += 1

	print "Case #%d: %d" % (case_no, answer)
