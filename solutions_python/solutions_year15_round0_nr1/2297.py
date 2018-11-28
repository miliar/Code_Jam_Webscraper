def q0(inputstring):
	inputs = inputstring.split()
	aud = inputs[1]

	audsize = 0
	friends = 0
	for index,member in enumerate(aud):
		if index > audsize:
			friends += index - audsize
			audsize = index
		audsize += int(member)
	return friends

def runtest(workfile):
	f = open(workfile,'r')
	tests = int(f.readline())
	write = open('out.txt','w')
	for i in range(tests):
		output = q0(f.readline())
		write.write("Case #%d: %d\n" % ((i+1),output))

print(runtest('A-large.in'))
