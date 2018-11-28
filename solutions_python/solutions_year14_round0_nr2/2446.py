input_file = open('B-large.in', 'r')
num_test_cases = int(input_file.readline().strip())
output_file = open('output_file_large.txt', 'w')
output = []
count = 1
for line in input_file:
	line = line.strip()
	C, F, X = [float(i) for i in line.split(' ')]
	rate = float(2)
	future_rate = rate + F
	t_time = 0
	while X/rate > C/rate + X/future_rate:
		t_time = t_time + (C/rate)
		rate = future_rate
		future_rate = rate + F

	t_time = t_time + (X/rate)
	output.append("Case #%d: %.7f" %(count, t_time))
	count = count + 1
	
	
output_file.write('\n'.join(output))
output_file.close()
input_file.close()