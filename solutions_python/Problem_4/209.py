#problem a
import sys

def parseArgv():
	input = sys.argv[1]
	output = sys.argv[2]
	return (input, output)

def minscprod(v1, v2):
	# len(v1) == len(v2)
	n = len(v1)
	minv2, maxv1 = [], []
	print str(v1), str(v2)
	for i in range(n):
		# get max v1 and min v2
		maxv1.append(max(v1))
		v1.remove(max(v1))
		minv2.append(min(v2))
		v2.remove(min(v2))
		print '%d, %d' % (maxv1[i], minv2[i])
	
	scalar_product = 0
	for i in range(n):
		scalar_product += (maxv1[i] * minv2[i])
	return scalar_product

# Main program starts here
filenames = parseArgv()
input = open(filenames[0], 'r')
output = open(filenames[1], 'w')

cases = input.readlines()
n_cases = int(cases.pop(0))

for case in range(n_cases):
	n = cases.pop(0)
	print 'n: ' + str(n)
	print 'cases[0] = ' + str(cases[0])
	v1 = [int(v) for v in cases[0].split()]
	v2 = [int(v) for v in cases[1].split()]
	print 'v1: ' + str(v1)
	print 'v2: ' + str(v2)

	del(cases[0:2])
	output.write('Case #%d: %d\n' % (case+1, minscprod(v1, v2)))

print 'Input processed! Now closing...'
input.close()
output.close()
