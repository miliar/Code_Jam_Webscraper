import sys

def cookie(C,F,X):
	rate = 2.0
	time = 0
	running = True
	while running:
		time_to_buy = C/rate
		rate_next = rate + F
		temp_time = X/rate
		temp_time1 = time_to_buy + X/rate_next
		if temp_time < temp_time1:
			time = time + temp_time
			running = False
		else:
			time = time + time_to_buy
			rate = rate_next
	return time

def parse_data(directory):
	f = open(directory, "r")
	output = open('output1.txt', 'w')
	cases = int(f.readline())
	for i in range(cases):
		list1 = f.readline().split()
		C = float(list1[0])
		F = float(list1[1])
		X = float(list1[2])
		time = cookie(C, F, X)
		output_str = "Case #%d: %.7f\n" %(i+1, time)
		output.writelines(output_str)
	f.close()
	output.close()

if __name__ == '__main__':
	directory = sys.argv[1]
	parse_data(directory)