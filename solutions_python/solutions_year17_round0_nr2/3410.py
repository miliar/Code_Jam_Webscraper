def get_tidy(s):
	accum = ""
	nines = False
	for i in range(0, len(s)-1):
		if nines:
			accum += '9'
			continue
		first = s[i]
		second = s[i+1]
		first_int = int(first)
		second_int = int(second)

		if (first_int > second_int):
			j = i-1
			if j < 0 or s[j] != first:
				accum += str(first_int-1)
			else:
				while j>=0 and s[j] == first:
					accum = accum[:j] + '9' + accum[j+1:]
					j -= 1
				accum = accum[:j+1] + str(int(s[j+1])-1) + accum[j+1:]
			nines = True
		else:
			accum += first

	if nines:
		accum += '9'
	else:
		accum += s[-1]
	return str(int(accum))


if __name__ == "__main__":
	N = int(raw_input())
	for i in range(1, N+1):
		line = raw_input()
		print "Case #{}: {}".format(i, get_tidy(line))
