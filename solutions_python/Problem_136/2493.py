import sys

if len(sys.argv) != 2:
	print "Usage {} <input_file_name>".format(sys.argv[0])
	sys.exit()

input_file = open(sys.argv[1], 'r')
input_data = input_file.read().split('\n')
input_file.close()


num_of_test_cases = int(input_data[0])

INITIAL_COOKIE_RATE = 2.0

for i in xrange(1, num_of_test_cases + 1):

	C, F, X = map(lambda x: float(x) ,input_data[i].split(" "))

	time = 0.0
	CPS = INITIAL_COOKIE_RATE
	
	while True:
		interval_length = C / CPS
		time += interval_length


		time_to_X = (X - C) / CPS
		time_to_X_with_new_farm = X / (CPS + F)

		if time_to_X <= time_to_X_with_new_farm:
			time += time_to_X 
			break
		else:
			CPS += F



	print "Case #{}: {}".format(i, time)