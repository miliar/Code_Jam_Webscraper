import math
from time import time, clock

INPUT_FILE = "./input3.txt"

RESULT = ""

fair_cache = {}
square_cache = {}

def is_fair(number):
	return number == int(str(number)[::-1])

def is_fair_cached(number):
	if number in fair_cache:
		return fair_cache[number]

	fair_cache[number] = is_fair(number)
	return fair_cache[number]

def is_square_cached(number):
	if number in square_cache:
		return square_cache[number]

	square_cache[number] = is_square(number)
	return square_cache[number]

def is_square(number):
	root = math.sqrt(number)

	if math.modf(root)[0] == 0.0 and is_fair(int(root)):
		return True
	return False

if __name__ == "__main__":

	# input file
	lines = [line.strip() for line in open(INPUT_FILE) if line.strip()]

	print "Total entries: ", lines[0]
	print "Total lines: ", len(lines)

	curPos = 1

	# read boards
	for boardNum in xrange(int(lines[0])):
		RESULT += "Case #" + str(boardNum + 1) + ": "

		dimensions = lines[curPos].split()
		curPos += 1

		start = long(dimensions[0])
		end = long(dimensions[1])

		print "Dimensions ["+ dimensions[0] + ", " + dimensions[1] + "]" 
		count = 0
		pos = start

		start_time = time()

		# only consider palindromes
		while pos != end + 1:
			if is_fair(pos) and is_square(pos):
				count += 1
			pos += 1

		print "Took ", time() - start_time, "seconds"
		RESULT += str(count)
		RESULT += "\n"

	#print
	#print "==================================="
	#print RESULT
	#print "==================================="

	output = open('./output3.txt','w')
	output.write(RESULT)
	output.close()