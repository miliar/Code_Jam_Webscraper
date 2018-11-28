__author__ = 'Llostris'

input_filename = 'input2.txt'
output_filename = 'output2.txt'

def form_output(testcase, time):
	# print "Case #%d: %f" % (testcase, time)
	with file(output_filename, 'a') as output:
		output.write("Case #%d: %f\n" % (testcase, time))


def cookie_shortest_time(testcase, cookies_for_farm, extra_cookies_per_farm, cookies_to_win,
						cookies_per_second=2,time_total=0) :

	solution1 = cookies_for_farm / cookies_per_second
	solution2 = cookies_to_win / cookies_per_second
	while solution1 + (cookies_to_win / ( cookies_per_second + extra_cookies_per_farm)) < solution2 :
		cookies_per_second += extra_cookies_per_farm
		time_total += solution1
		solution1 = cookies_for_farm / cookies_per_second
		solution2 = cookies_to_win / cookies_per_second

	form_output(testcase, time_total + solution2)


def cookie_shortest_time_recursive(testcase, cookies_for_farm, extra_cookies_per_farm, cookies_to_win,
						cookies_per_second=2,time_total=0) :
	solution1 = cookies_for_farm / cookies_per_second
	solution2 = cookies_to_win / cookies_per_second

	if solution1 + (cookies_to_win / ( cookies_per_second + extra_cookies_per_farm)) > solution2:
		form_output(testcase, time_total + solution2)
	else:
		cookie_shortest_time(testcase,
							 cookies_for_farm, extra_cookies_per_farm, cookies_to_win,
							 cookies_per_second + extra_cookies_per_farm, time_total + solution1)


if __name__ == '__main__' :
	input_file = open(input_filename)
	input_data = input_file.readlines()
	testcases = int(input_data.pop(0))

	file(output_filename, 'w+').close()

	for i in range(testcases) :
		data = map(float, input_data.pop(0).split())
		cookie_shortest_time(i + 1, data[0], data[1], data[2])
		input_file.close()