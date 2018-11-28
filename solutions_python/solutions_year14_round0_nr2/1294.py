infile = open("B-large.in", "r")

f = open('outp2.txt', 'w')
cases = infile.read().strip().split("\n")
nb_cases = cases[0][0]
cases = cases[1:]
i = 1
for case in cases:
	string_to_add = ""
	cookies_per_second = ""
	cookies_to_buy = ""
	cookies_to_win = ""
	for char in case:
		if char != " ":
			string_to_add = string_to_add + char
		else:
			if cookies_to_buy == "":
				cookies_to_buy = string_to_add
				string_to_add = ""
			elif cookies_per_second == "":
				cookies_per_second	= string_to_add
				string_to_add = ""
	cookies_to_win = string_to_add
	gain_per_second = 2
	farms = 0
	seconds_spent = 0
	seconds_to_win_without_new_farm = float(cookies_to_win) / float(gain_per_second)
	seconds_spent_to_buy = float(cookies_to_buy) / gain_per_second
	seconds_to_win_with_new_farm = (float(cookies_to_win) / (float(gain_per_second) + float(cookies_per_second))) + seconds_spent_to_buy
	win = False
	while win == False:
		if seconds_to_win_with_new_farm < seconds_to_win_without_new_farm:
			farms = farms + 1
			seconds_spent = seconds_spent + seconds_spent_to_buy
			gain_per_second = gain_per_second + float(cookies_per_second)
			seconds_to_win_without_new_farm = seconds_to_win_with_new_farm
			seconds_spent_to_buy = float(cookies_to_buy) / gain_per_second
			seconds_to_win_with_new_farm = float(cookies_to_win) / (gain_per_second+float(cookies_per_second)) + seconds_spent + seconds_spent_to_buy
		else:
			win = True
			print >> f, "Case #%s: %.7f" % (i, round(seconds_to_win_without_new_farm, 8))
			i = i + 1
f.close()
