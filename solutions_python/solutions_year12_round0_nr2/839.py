import math
import sys

def main():
	file_read = open(sys.argv[1], 'r')
	lines = file_read.readlines()	
	no_test_cases = int(lines[0])
	for k in range(no_test_cases):		
		input = lines[k+1].split()
		no_samples = int(input[0])
		no_surp_allowed = int(input[1])
		threshold = int(input[2])
		surp_thres = (threshold*3)-4
		unsurp_threshol = ((threshold-1)*3)+1
		if surp_thres < 0:
			surp_thres = 1
		if unsurp_threshol < 0:
			unsurp_threshol = 1
		if threshold == 0:
			surp_thres = unsurp_threshol = 0
		samples = [] ; no_surp = 0 ; no_unsurp = 0
		for j in range(no_samples):
			samples.append(int(input[3+j]))
		for j in range(no_samples):			
			if samples[j] >= surp_thres:
				no_surp += 1
			if samples[j] >= unsurp_threshol:
				no_unsurp += 1
		output = min(no_surp, no_unsurp+no_surp_allowed)
		print "Case #" + str(k+1) + ":",
		print output
		

if __name__ == '__main__':
	main()