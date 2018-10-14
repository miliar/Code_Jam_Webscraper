filename = "A-large.in"
data = [line.split(" ") for line in open(filename).read().split("\n")][0:-1]
t = int(data[0][0])
data = [(int(line[0]),int(line[1])) for line in data[1:]]

for (id, (n,k)) in enumerate(data):
	if k % 2**n == (2**n - 1):
		answer = "ON"
	else:
		answer = "OFF"
	print "Case #%d: %s" % (id + 1, answer)

