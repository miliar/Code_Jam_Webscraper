
def solve_it(inputdata):
	lines = input_data.split('\n')
	#print lines
	num_cases = int(lines[0])
	for i in range(num_cases):
		data = lines[i+1].split()
		C = float(data[0])
		F = float(data[1])
		X = float(data[2])
		time = 0.0
		buy = True
		rate = 2.0
		y =0.0
		while buy:
			if (C-y) < (X-y):
				if (X-y)/rate > (C-y)/rate + (X)/(rate+F):
					y=0
					time += (C-y)/rate
					rate+=F					
				else:
					time +=(X-y)/rate
					buy = False
			else:
				time +=(X-y)/rate
				buy = False

		print  "Case #%d: %.8f" % (i+1,time)	
	
	return


import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        input_data_file = open(file_location, 'r')
        input_data = ''.join(input_data_file.readlines())
        input_data_file.close()
        solve_it(input_data)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/fl_16_2)'
