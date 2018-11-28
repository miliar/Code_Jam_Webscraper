import sys

input = open(sys.argv[1], 'r')
output = open(sys.argv[2], 'w')

cases = input.readline()
cases = int(cases)

for x in range(cases):
	cnum = int(input.readline())
	candies = input.readline().split()
	for y in range(len(candies)):
		candies[y] = int(candies[y])
	xsum = 0
	for z in candies:
		xsum = xsum ^ z
	
	if xsum: 
		output.write("Case #%i: NO\n" % (x+1))
	
	else:
		candies.sort()
		output.write("Case #%i: %i\n" % (x+1, sum(candies[1:])))
	
#	print xsum

#	output.write("Case #%i: %i\n" % (x+1, ANSWER_VARIABLE_NAME))

input.close()
output.close()


