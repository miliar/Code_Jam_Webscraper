# Qualification Round 2012
# Problem B. Dancing With the Googlers

import sys

def reverse_numeric(x, y):
	return int(y) - int(x)

def processScores(line):
	scores = line.rsplit(' ')
	
	num_of_dancers = int(scores.pop(0))
	num_of_surprises = int(scores.pop(0))
	min_best_score = int(scores.pop(0))
	
	if min_best_score == 0:
		counter = len(scores)
	else:
		counter = 0
		
		for score in sorted(scores, cmp=reverse_numeric):
			score = int(score)
			if score > 0:
				div = score / 3
				remainder = score - div * 3
				
				if div >= min_best_score:
					counter += 1
				else:
					if div >= max(min_best_score - 2, 0):
						if remainder == 0 and min_best_score - div == 1 and num_of_surprises > 0:
							counter += 1
							num_of_surprises -= 1
						elif remainder == 1 and min_best_score - div == 1:
							counter += 1
						elif remainder == 2 and min_best_score - div == 1:
							counter += 1
						elif remainder == 2 and min_best_score - div == 2 and num_of_surprises > 0:
							counter += 1
							num_of_surprises -= 1					
					else:
						break
			else:
				break
				
	return counter

def main():
	f_in = open(sys.argv[1], "rb")
	line = f_in.readline()

	# Getting total number of test cases
	total_tc_num = int(line.rstrip())
	count = 1

	# Processing input test cases
	if total_tc_num > 0:
		f_out = open(sys.argv[2], "w")
		while line and count <= total_tc_num:
			line = f_in.readline().rstrip()
			str = "Case #%d: %s" % (count, processScores(line))
			if count < total_tc_num:
				str += "\n"
			f_out.write(str)
			count += 1
		f_out.close()
	f_in.close()

if __name__ == '__main__' :
    main()