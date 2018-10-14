input_file = open('/Users/Aida/Desktop/googlecodejam/input_cookie.txt')
output_file = open('/Users/Aida/Desktop/googlecodejam/output_cookie.txt', 'w')

T = int(input_file.readline()) # number of test cases

i =1

while i <= T:
	new_case = input_file.readline().split()
	
	C = float(new_case[0])
	F = float(new_case[1])
	X = float(new_case[2])
	final_time = 0.0000000000
	time_passed = 0.000000000
	potential_time = 0.0000000000
	current_time = 0.000000000
	current_rate = 2.0
	status = 'no'
	while status == 'no':
		current_time = (X / current_rate) + time_passed
		potential_time = (X / (current_rate + F)) + (C / current_rate) + time_passed
		if current_time <= potential_time:
			status ='yes'
			final_time = current_time
		else:
			time_passed += C / current_rate
			current_rate += F

	output_file.write("Case #" + str(i) + ": " + str(float(final_time)))

	i +=1
	if i<= T:
		output_file.write("\n")

input_file.close()
output_file.close()