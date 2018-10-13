def get_win_time(farms_to_buy, c, f, x):



	return time + (x / cookies_per_second)


def get_best_time(c, f, x):

	# Floatify inputs
	c = float(c)
	f = float(f)
	x = float(x)

	time = 0
	cookies_per_second = 2

	while (True):

		# time until victory
		tuv = time + (x / cookies_per_second)
		# time until victory with next farm
		tuf = (time + (c / cookies_per_second)) + (x / (cookies_per_second + f))

		if tuv <= tuf:
			return tuv

		time += c / cookies_per_second
		cookies_per_second += f


# Get data
file = open('in','r')
data = file.read().splitlines()
file.close()


# Start solving
results = []
test_cases = int(data[0])
for i in range(test_cases):
	numbers = data[i+1].split()
	results.append(
		get_best_time(
			numbers[0],
			numbers[1],
			numbers[2])
	)

# print results
file = open('out', 'w')
for i in range(test_cases):
	num = "%5f" % results[i]
	file.write('Case #' + str(i + 1) + ': ' + num + '\n')
file.close()
