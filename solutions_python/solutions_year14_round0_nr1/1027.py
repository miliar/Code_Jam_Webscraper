if __name__ == "__main__":
	with open("A-small-attempt0.in", 'r') as inputf:
		outputf=open("A_out.out",'w')
		line=inputf.readline()
		line=line.rstrip('\n')
		test_num=int(line)
		
		for test in range(test_num):

			line=inputf.readline()
			line=line.rstrip('\n')
			first_ans=int(line)

			for lines in range(4):
				line=inputf.readline()
				if lines==first_ans-1:
					line=line.rstrip('\n')
					first_line=line.split(' ')

			line=inputf.readline()
			line=line.rstrip('\n')
			second_ans=int(line)

			for lines in range(4):
				line=inputf.readline()
				if lines==second_ans-1:
					line=line.rstrip('\n')
					second_line=line.split(' ')

			match_num=0
			match=''
			for index in range(4):
				if second_line[index] in first_line:
					match_num=match_num+1
					match=second_line[index]
					if match_num > 1:
						result="Case #%d: Bad magician!" % (test+1)
						outputf.write(result)
						break
			if match_num == 1:
				result="Case #%d: %s" % (test+1, match)
				outputf.write(result)
			elif match_num == 0:
				result="Case #%d: Volunteer cheated!" % (test+1)
				outputf.write(result)

			if test!=test_num-1:
				outputf.write('\n')




		
