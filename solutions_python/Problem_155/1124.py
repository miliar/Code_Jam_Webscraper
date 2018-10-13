fin = open("A-large.in", "r")
fout = open("ovation.out", "w")

tests = int(fin.readline().strip())
# print tests

for test in xrange(1, tests+1):
	s_max, string = fin.readline().strip().split()
	# print s_max
	# print string
	string = [int(s) for s in string]
	# print string
	stands = int(string[0])
	invites = 0
	for shyness in xrange(1, int(s_max)+1):
		if shyness - stands > invites:
			invites = shyness - stands
		stands += string[shyness]

	answer = "Case #" + str(test) + ": " + str(invites)
	fout.write(answer + "\n")



fin.close()
fout.close()