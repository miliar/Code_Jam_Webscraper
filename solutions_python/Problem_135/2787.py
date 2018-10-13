



def solve_it(inputdata):
	lines = input_data.split('\n')
	#print lines
	num_cases = int(lines[0])
	
	for i in range(num_cases):
		g1 = int(lines[1+i*10])
		cand1 = lines[1+10*i+g1].split()
		g2 = int(lines[1+i*10+5])
		cand2 =  lines[1+10*i+5+g2].split()
		res = list(set(cand1).intersection(cand2))
		#print cand1, cand2, res
		if len(res) < 1:
			print "Case #%d: Volunteer cheated!" %(i+1)
		elif len(res)>1:
			print "Case #%d: Bad magician!"%(i+1)
		else:
			print "Case #%d: %d" % (i+1,int(res[0]))

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
