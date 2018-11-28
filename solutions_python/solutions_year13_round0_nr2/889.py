# -*- coding: utf-8 -*-

import io

def main():
	results = []
	#with io.open("B-small-attempt0.in", "r") as f:
	with io.open("B-large.in", "r") as f:
		testcase_count = f.readline()
		for testcase in range(int(testcase_count)):
			field = []

			digits = f.readline().split(' ')
			n = int(digits[0])
			m = int(digits[1])

			for col in range(n):
				field.append([])
				digits = f.readline().split(' ')

				for digit in digits:
					field[col].append(int(digit))

			""" for debug
			for row in range(n):
				line = ""
				for col in range(m):
					line += "{0:d} ".format(field[row][col])
				print(line)
			#"""

			impossible = False
			for row in range(n):
				for col in range(m):
					digit = field[row][col]

					greater_exist_in_horizontal = False
					# check horizontally for greater digit
					for i in range(m):
						if i != col and field[row][i] > digit:
							greater_exist_in_horizontal = True
							break

					greater_exist_in_vertical = False
					# check vertically for greater digit
					for i in range(n):
						if i != row and field[i][col] > digit:
							greater_exist_in_vertical = True

					if greater_exist_in_horizontal and greater_exist_in_vertical:
						impossible = True
						break
				if impossible:
					break

			if impossible:
				results.append("Case #{0}: NO".format(testcase + 1))
			else:
				results.append("Case #{0}: YES".format(testcase + 1))


	#with io.open("B-smallset-attempt0.out", "w", encoding="utf-8") as f:
	with io.open("B-large.out", "w", encoding="utf-8") as f:
		for i in range(len(results)):
			f.write(results[i])
			if i != len(results) - 1:
				f.write('\n')

if __name__ == "__main__":
	main()
