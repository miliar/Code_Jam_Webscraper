# Qualification Round 2012
# Problem C. Recycled Numbers

import sys

def processNums(line):
	already_checked = {}
	counter = 0
	
	nums = line.rsplit(' ')
	digits = len(nums[0])
	
	A = int(nums[0])
	B = int(nums[1])
	
	num = A
	while num <= B:
		if not num in already_checked:
			numstr = str(num)
			num_pairs = {}
			i = 1
			while i < digits:
				if numstr[-i] != '0':
					pairstr = numstr[-i:] + numstr[:digits-i]
					if pairstr not in num_pairs and int(numstr) < int(pairstr) and int(pairstr) <= B:
						already_checked[pairstr] = 1
						num_pairs[pairstr] = 1
						counter += 1
				i += 1
		num += 1
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
			str = "Case #%d: %s" % (count, processNums(line))
			if count < total_tc_num:
				str += "\n"
			f_out.write(str)
			count += 1
		f_out.close()
	f_in.close()

if __name__ == '__main__' :
    main()