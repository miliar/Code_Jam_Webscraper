def process(digits):
	lastdigit = digits[0]
	lastindex = 0
	N = len(digits)
	for i in range(N):
		if digits[i] > lastdigit:
			lastdigit = digits[i]
			lastindex = i
		if digits[i] < lastdigit:
			if lastdigit == 1:
				return [9]*(N-1)
			return digits[:lastindex] + [lastdigit-1] + [9]*(N-lastindex-1)
	return digits


def run():
	T = int(raw_input().strip())
	for caseno in range(T):
		digits = map(int, list(raw_input().strip()))
		results = ''.join(map(str, process(digits)))
		print('Case #' + str(caseno+1) + ': ' + results)

run()

