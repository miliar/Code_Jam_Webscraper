import csv

def main():
	num_test_cases = 0
	test_cases = {}

	with open('A-small-attempt0.in', 'rb') as f:
		reader = csv.reader(f, delimiter=' ')

		num_test_cases = int(reader.next()[0])

		# print num_test_cases

		for x in range(0,num_test_cases):

			# start = x * 10
			# end = (x+1) * 10

			# test_case = []

			# for y in range(start, end):
			# 	test_case.append(map(int, reader.next()))

			# test_cases[x] = test_case

			# next() once: first row selection
			row1 = None
			row2 = None
			row_select1_num = int(reader.next()[0])

			# next() 4 times: 4 rows

			for y in range(1, 5):
				row = map(int, reader.next())
				if y == row_select1_num:
					row1 = row

			# next() once: second row selection

			row_select2_num = int(reader.next()[0])

			# next() 4 times: 4 rows

			for y in range(1, 5):
				row = map(int, reader.next())
				if y == row_select2_num:
					row2 = row


			# print row_select1_num, row1
			# print row_select2_num, row2

			intersection = set(row1) & set(row2)

			if len(intersection) == 0:
				print "Case #" + str(x+1) + ": Volunteer cheated!"

			elif len(intersection) > 1:
				print "Case #" + str(x+1) + ": Bad magician!"

			elif len(intersection) == 1:
				print "Case #" + str(x+1) + ": " + str(intersection.pop())



if __name__ == "__main__":
    main()