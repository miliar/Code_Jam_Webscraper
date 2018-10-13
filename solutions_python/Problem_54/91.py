def gcd(a, b):
	if (b == 0):
		return a
	else:
		return gcd(b, a % b)

input_file = open('in.txt', 'r')
output_file = open('out.txt', 'w')
line = input_file.readline()
C = int(line)
for c in range(0, C):
	line = input_file.readline()
	split = line.split()
	N = int(split[0])
	list = []
	for i in range(1, N+1):
		list.append(int(split[i]))
	list.sort()
	#print(list)
		
	diffGCD = list[1] - list[0]
	for i in range(2, len(list)):
		diffGCD = gcd(diffGCD, list[i] - list[i - 1])

	if list[0] % diffGCD == 0:
		shift = 0
	else:
		shift = diffGCD - (list[0] % diffGCD)
	print("Case #%d: %d" % (c+1, shift))
	output_file.write("Case #%d: %d\n" % (c+1, shift))

output_file.close()