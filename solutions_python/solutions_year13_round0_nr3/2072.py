def ReverseNumber(n, partial=0):
    if n == 0:
        return partial
    return ReverseNumber(n / 10, partial * 10 + n % 10)

def read(path):
	output = open('googlers.in', 'w')
	x = 1
	f = open(path)
	line = f.readline()
	for line in f:
		line = line.strip("\n")
		ends = line.split(" ")
		low = int(ends[0])
		high = int(ends[1])
		num = low
		fairsqrs = 0
		while num <= high:
			root = int(math.sqrt(num))
			
			if ReverseNumber(num) == num and ReverseNumber(root) == root and root * root == num:
				fairsqrs += 1
			num += 1
		output.write("Case #" + str(x) + ": " + str(fairsqrs))
		output.write("\n")
		line = f.readline
		x += 1
	output.close()