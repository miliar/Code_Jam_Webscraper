# Qualification Round 2012
# Problem A. Speaking in Tongues

import re
import sys

sample_input = """
zq
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
"""
sample_output = """
qz
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up
"""

abc_mapping = {}

def googlereseToEnglish(googlerese):
	global abc_mapping
	
	english = ""
	
	for letter in googlerese:
		if letter in abc_mapping:
			english += abc_mapping[letter]
		else:
			english += letter
	
	return english

def main():
	global sample_input
	global sample_output
	global abc_mapping
	
	for i in range(len(sample_input)):
		if re.match(r"[a-z]", sample_input[i]):
			abc_mapping[sample_input[i]] = sample_output[i]

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
			str = "Case #%d: %s" % (count, googlereseToEnglish(line))
			if count < total_tc_num:
				str += "\n"
			f_out.write(str)
			count += 1
		f_out.close()
	f_in.close()

if __name__ == '__main__' :
    main()