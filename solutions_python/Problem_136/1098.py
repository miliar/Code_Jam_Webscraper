T = input()

for case in range(1, T + 1):
	C, F, X = map(float, raw_input().split())

	cookies = 0
	production = 2.0
	time = 0

	while True:
		# print '#', X / production, (X + C) / production
		if (X - cookies) / production <= (C - cookies) / production +  X / (production + F):
			time += (X - cookies) / production
			break

		# build a farm
		if cookies >= C:
			cookies -= C
			production += F
		else:
			time += (C - cookies) / production
			production += F
			cookies = 0

		# print time, production, cookies

	print "Case #%d:" % case, time