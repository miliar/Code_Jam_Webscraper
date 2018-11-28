""" Output a file. 
For each test case, output one line containing "Case #x: y", 
where x is the test case number (starting from 1) 
and y is the minimum number of friends you must invite.

Call as 
python a.py input
in Terminal
"""

import sys
firstArgument = sys.argv[1]

def output(fileName = firstArgument):
	try:
		fRead = open(fileName, 'r') # Read the file into fRead
		i = 1 						# The line number.
		testCaseNumebr = 0			# The number of test cases
		result = []					# The output result
		for line in fRead.readlines():

			standingPeople = 0		# The number of people standing
			peopleNeeded = 0		# The number of people needed

			if (i == 1):
				testCaseNumebr = line	# The number of test cases

				#print 'There are ' + str(testCaseNumebr) + ' test cases'

			else:

				#print 'Going into case ' + str(i-1)

				index = line.find(' ')	# The index of the space
				Smax = line[:index]		# The Smax
				details = line[index+1:]	# The detailed list

				for x in range(int(Smax) + 1):	# x is the shyness of the current people
					#print 'Current shyness is ' + str(x) + ' and there are ' + str(standingPeople) + ' standing'

					if (details[x] != 0):
						if (standingPeople < x):	# If the standingPeople is less than the current shyness
							tmp = x - standingPeople
							peopleNeeded += tmp	# To make the following people standing
							standingPeople += tmp

						standingPeople += int(details[x])	# People stands

				#print 'Case #' + str(i-1) + ': ' + str(peopleNeeded)		# The output
				resultString = 'Case #' + str(i-1) + ': ' + str(peopleNeeded) + '\n'
				result = result + [resultString]
			i += 1					# Proceeding to next line
	finally:
		if fRead:
			fRead.close()
		# Write into file
		print result

		out = open('out.txt', 'w')
		for caseResult in result:
			out.write(caseResult)

		out.close()


if __name__ == "__main__":
	output();