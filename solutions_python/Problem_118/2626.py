
import sys
import math

def checkIsPalindrome(string):
	# Reverse the string and check if it is equal
	return string == string[::-1]

def isIntCheck(a):
	b = math.sqrt(a)
	c = round(b) * round(b)

	if a == c and checkIsPalindrome(str(int(b))):
		#print a
		#print b
		return True
	else:
		return False

def init():

	filename = sys.argv[1]

	try:

		fp = open(filename, "r")

	except IOError, e:

		print 'Opening filename does not exist!'
		sys.exit(0)

	else:

		# Get the size of test cases
		num = fp.readline()

		case = 1

		while 1:

			if case <= int(num):
				line = fp.readline().rstrip('\n').split(" ")
				#print line
				(lb, ub) = line[0:2]
				lb = int(lb)
				ub = int(ub)

				#print "%d >> %d" % (lb, ub)

				count = 0

				current = int(lb)
				while current <= ub:
					result = checkIsPalindrome(str(current))
					#print "%d, %r" % (current, result)
					if result == True:
						if (isIntCheck(current) == True):
							#print current
							count += 1
					current += 1

				print "Case #%d: %d" % (case, count)
				case += 1
			else:
				break;
init()