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

			row1 = int(str(lines.next()).rstrip())
			
			row = 1
			while row <= row1:
			 	set1 = set(lines.next().rstrip().split(" "))
			 	row += 1

			while row <= 4:
				dummy = lines.next()
				row += 1

			row2 = int(str(lines.next()).rstrip())

			row = 1
			while row <= row2:
			 	set2 = set(lines.next().rstrip().split(" "))
			 	row += 1

			while row <= 4:
				dummy = lines.next()
				row += 1

			result = set1 & set2

			if len(result) == 1:
				result = int(list(result)[0])
				print "Case #%d: %d" % (i, result)
			elif len(result) == 0:
				print "Case #%d: %s" % (i, "Volunteer cheated!")
			else:
				print "Case #%d: %s" % (i, "Bad magician!")
			


if __name__ == "__main__":
	main(sys.argv)