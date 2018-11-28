import sys

def isLightOn(n, k):
	snappers = []
	for i in range(n):
		snappers.append(False)
	for i in range(k):
		end = 0
		while end+1 < len(snappers) and snappers[end] == True:
			end = end + 1
		for j in range(end+1):
			snappers[j] = not snappers[j]
	for snapper in snappers:
		if not snapper:
			return False
	return True

input = open(sys.argv[1])
output = open(sys.argv[2], 'w')

caseCount = int(input.readline())

for i in range(caseCount):
	line = input.readline().split()
	n = int(line[0])
	k = int(line[1])
	result = isLightOn(n, k)
	output.write('Case #'+str(i+1)+': ')
	if result:
		output.write('ON\n')
	else:
		output.write('OFF\n')

input.close()
output.close()