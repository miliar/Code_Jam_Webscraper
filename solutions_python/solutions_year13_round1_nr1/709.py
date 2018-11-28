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

		# my_sq_list = []
		# for i1 in xrange(1, 1001):
		# 	my_sq_list.append(i1 ** 2)

		for i in xrange(1, T + 1):			
			rt = map(int, lines.next().rstrip().split(" "))

			r = rt[0]
			t = rt[1]

			i1 = r
			count = 0
			while True:

				t -= (i1 + 1) ** 2 - i1 ** 2
				i1 += 2
				# print t, count

				if t >= 0:
					count += 1
					# print t
				else:
					break

			print "Case #%d: %d" % (i, count)


if __name__ == "__main__":
	main(sys.argv)