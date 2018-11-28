def parseline(line):
	a = line.split(" ")
	return a[1]

def calculate(string):
	current_standing = int(string[0])
	friend_required = 0
	l = len(string)
	for i in range(1,l-1):
		if current_standing >= i :
			current_standing += int(string[i])
		else:
			friend_required += (i - current_standing)
			current_standing = i + int(string[i])

	return friend_required


f = open("input.txt", "r")
k = open("output.txt", "w")
t = int(f.readline())

for i in xrange(t):
	string = parseline(f.readline())
	res = "Case #%d: %d\n" % (i+1, calculate(string))
	k.write(res)
