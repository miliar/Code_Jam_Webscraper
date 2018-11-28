import string

cases = int(raw_input())


for case in range(cases):
	answer = ""

	N = raw_input()

	index = 0
	while True:
		for i in range(10):
			test = str(i) * (len(N)-index)
			if int(answer + test) > int(N):
				break
			last = test

		answer += last[0]
		if len(answer) == len(N):
			answer = string.lstrip(answer,"0")
			break

		index += 1

	print "Case #" + str(case+1) + ": " + answer


