import sys

data = []
with open(sys.argv[1], 'r') as f:
	for line in f:
		data.append(line.strip('\n'))
case = 1
while case < len(data):
	length, shyness = data[case].split(' ')
	res, standing = 0, 0
	for i in range(int(length)+1):
		x = int(shyness[i])
		if standing < i:
			res += i - standing
			standing = i
		standing += x
	print "Case #%d: %d" % (case, res)
	case+=1