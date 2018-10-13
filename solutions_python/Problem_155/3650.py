__author__ = 'Kenneth'

def printOut(num,out,file):
	file.write("Case #%d: %d\n" % (num,out))


input_file = open('A-small-attempt0.in.txt')
output_file = open('out.txt','w')
num_cases = int(input_file.readline())


print num_cases
for case in xrange(1,num_cases+1):
	num_levels = int(input_file.read(1))
	toAdd = 0
	currentOvation = 0
	#skip space
	input_file.read(1)


	for level in xrange(0,num_levels+1):
		OvAtLevel = int(input_file.read(1))

		if currentOvation >= level:
			currentOvation += OvAtLevel
		else:
			toAdd += level - currentOvation
			currentOvation += OvAtLevel + level - currentOvation
	input_file.read(1)
	printOut(case,toAdd,output_file)


input_file.close()
output_file.close()