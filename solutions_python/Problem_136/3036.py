for case in range(int(input())):
	c, f, x = map(float, input().split())
	cookies_per_second, seconds = 2.0, 0.0
	answer = x / cookies_per_second
	while True:
		seconds = seconds + (c / cookies_per_second)
		cookies_per_second = cookies_per_second + f
		temp_answer = seconds + (x / cookies_per_second)
		if temp_answer > answer:
			break
		answer = temp_answer
	print("Case #%d: %.7f" % (case + 1, answer))