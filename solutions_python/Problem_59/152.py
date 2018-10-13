inFile="/home/se/Downloads/A-large.in"

input = open(inFile)
output = open("/home/se/Downloads/test.out", "w")

line = input.readline().strip()
cases = int(line)


for case in range (0, cases):
	dir = {}

	count = 0

	line = input.readline().strip()
	fields=line.split(" ")
	M=int(fields[0])
	N=int(fields[1])
	for dirs in range (0, M):
		line = input.readline().strip()
		entries=line.split("/")
		entries.pop(0)
		prev = ""

		for entry in entries:
			prev+= "/" + entry
			if  not (prev in dir):
				dir[prev] = 1

	
	for dirs in range (0,N):
		line = input.readline().strip()
		entries=line.split("/")
		entries.pop(0)
		prev = ""
	
		for entry in entries:
			prev+= "/" + entry
			if  not (prev in dir):
				dir[prev] = 1
				count+=1

	print >> output, "Case #%d: %d" % (case+1, count)


input.close()
output.close()

