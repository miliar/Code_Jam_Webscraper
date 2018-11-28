import sys



if __name__ == "__main__":
	file_in = sys.argv[1]
	file_out = sys.argv[2]

	with open(file_in,'r') as f_in:
		with open(file_out,'w') as f_out:
			testcases = int(f_in.readline())

			for i in range(testcases):
				first_row_num = int(f_in.readline())
				for j in range(4):
					line = f_in.readline()[0:-1]
					if first_row_num == (j + 1):
						first_row = line.split(' ')

				second_row_num = int(f_in.readline())
				for j in range(4):
					line = f_in.readline()[0:-1]
					if second_row_num == (j + 1):
						second_row = line.split(' ')

				# print 'First: %s\nSecond: %s' % (str(first_row),str(second_row))

				common = filter(lambda x: x in first_row,second_row)
				# print 'Common: %s' % str(common)

				if len(common) == 1:
					message = str(common[0])
				elif len(common) > 1:
					message = 'Bad magician!'
				elif len(common) < 1:
					message = 'Volunteer cheated!'

				message = 'Case #%d: %s\n' % (i + 1,message)
				f_out.write(message)



