from operator import itemgetter
import sys
import time


def main(argv):
	''' The main function '''
	#open the file
	with open(argv[1]) as f:
		#number of testcases
		T = int(f.readline().rstrip())
		lines = iter(f.readlines())

		for i in xrange(1, T + 1):
			nm = map(int, lines.next().rstrip().split(" "))
			n = nm[0]
			m = nm[1]

			# my_pat = [[100 for i2 in xrange(m)] for i3 in xrange(n)]
			my_pat = []
			for i1 in xrange(n):
				my_pat.append(lines.next().rstrip().split(" "))


			#check for palindromes
			row_flag = True
			col_flag = True

			col_max = [-1 for i1 in xrange(m)]
			row_max = [-1 for i1 in xrange(n)]

			for i1 in xrange(n):
				# print my_pat[i1]
				row_max[i1] = max(my_pat[i1])
			
			
			for i1 in xrange(m):
				my_list = []
				for i2 in xrange(n):
					my_list.append(my_pat[i2][i1])
				col_max[i1] = max(my_list)
			

			result = "YES"

			for i1 in xrange(n):
				for i2 in xrange(m):
					val = my_pat[i1][i2]
					# print val, row_max[i1], col_max[i2]
					if val != row_max[i1] and val != col_max[i2]:
						result = "NO"
						break

					

			print "Case #%d: %s" % (i, result)


if __name__ == "__main__":
	main(sys.argv)