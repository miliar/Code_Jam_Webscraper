from operator import itemgetter
import sys
import time
# from numpy import array, diag

#chek if indices are out of bounds
def out_of_bounds(row,col,dimensions):
	if row <0 or col < 0:
		return True
	if row >= dimensions[0] or col >= dimensions[1]:
		return True
	return False

def XO_row(my_list):
	''' row'''
	x_count = my_list.count('X')
	o_count = my_list.count('O')
	t_count = my_list.count('T')
	dot_count = my_list.count('.')

	if x_count == 4 or (x_count == 3 and t_count == 1):
		return 'x'
	if o_count == 4 or (o_count == 3 and t_count == 1):
		return 'o'
	if dot_count == 0:	
		return 0
	return 1

def XO_col(my_list):
 	return XO_row(my_list)	

def XO_princ_diag(my_list):
	return XO_row(my_list)
def XO_secdiag(my_list):
	return XO_row(my_list)


def main(argv):
	''' The main function '''
	#open the file
	with open(argv[1]) as f:
		#number of testcases
		T = int(f.readline().rstrip())
		lines = iter(f.readlines())

		for i in xrange(1, T + 1):
			# print i
			my_mat = [[" "] for i1 in xrange(4)]
			row1 = list(lines.next().rstrip())
			row2 = list(lines.next().rstrip())
			row3 = list(lines.next().rstrip())
			row4 = list(lines.next().rstrip())
			if i != T:
				row5 = list(lines.next().rstrip())

			my_mat[0] = row1
			my_mat[1] = row2
			my_mat[2] = row3
			my_mat[3] = row4

			# print my_mat[0][3]
			#check all rows
			result = ""
			dot_count = -1


			for i2 in xrange(4):
				r = XO_row(my_mat[i2])
				if r == 'x':
					result = "X won"
					break
				elif r == 'o':
					result = "O won"
					break
				else:
					if r > dot_count:
						dot_count = r

			#check all columns
			for i2 in xrange(4):
				my_list = []
				for i3 in xrange(4):
					
					my_list.append(my_mat[i3][i2])
					r = XO_col(my_list)

					if r == 'x':
						result = "X won"
						break
					elif r == 'o':
						result = "O won"
						break
			#check princ diag
			
			my_list = [my_mat[i4][j] for i4 in xrange(4) for j in xrange(4) if i4 == j]
			
			r = XO_princ_diag(my_list)

			if r == 'x':
				result = "X won"
				
			elif r == 'o':
				result = "O won"
				

			#check sec diag
			
			my_list = [my_mat[i4][j] for i4 in xrange(4) for j in xrange(4) if i4 + j == 3]
			

			r = XO_secdiag(my_list)

			if r == 'x':
				result = "X won"
				
			elif r == 'o':
				result = "O won"
				


			if not result:
				if dot_count:
					result = "Game has not completed"
				else:
					result = "Draw"
			# print i, row4, T

			print "Case #%d: %s" % (i, result)
			# print "Till here", i, T 

if __name__ == "__main__":
	main(sys.argv)