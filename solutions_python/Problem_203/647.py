import sys
import re

inputfile = open(sys.argv[1],'r')
outputfile = open(sys.argv[1].replace("in","out"),'w')

testcases = int(inputfile.readline())

for i in range (0,testcases):
	row_col = inputfile.readline()
	rows = int(row_col.split(" ")[0])
	cols = int(row_col.split(" ")[1])

	outputfile.write("CASE #" + str(i+1)+ ": \n")
	grid =[]
	for r in range(0,rows):
		grid.append(inputfile.readline())
		
	for r in range(0,rows):
		row = grid[r]
		alph_pattern = re.compile(r'.*(\?[A-Z]).*')
		alph_pattern_aft = re.compile(r'.*([A-Z]\?).*')
		ques_str = '\?' * cols
		ques_pattern = re.compile(ques_str)

		if ques_pattern.match(row):
			print "QS_ROW: %s" % row
			qu_index = r 
			if r > 0:
				row = grid[r-1]
			else:
				while ques_pattern.match(row):
					qu_index = qu_index + 1
					row = grid[qu_index]
					
				row = grid[qu_index]
		
		if alph_pattern.match(row):
			match = alph_pattern.match(row)
			while match:
				print "MATCH: %s" % match.group(0)
				str_match = match.group(1)
				str_match_new = str_match.replace('?',str_match[1])
				row = row.replace(str_match,str_match_new)
				match = alph_pattern.match(row)

		if alph_pattern_aft.match(row):
			match = alph_pattern_aft.match(row)
			while match:
				print "MATCH: %s" % match.group(1)
				str_match = match.group(1)
				str_match_new = str_match.replace('?',str_match[0])
				print "MATCH_NEW: %s"% str_match_new
				print "MATCH_OLD: %s"% str_match
				row = row.replace(str_match,str_match_new)
				print "ROW_NEW: %s"% row
				match = alph_pattern_aft.match(row)
		grid[r] = row
		outputfile.write(row)

	outputfile.write("\n")

