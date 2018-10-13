fin = open("C-small-attempt2.in", "r")
fout = open("dijkstra.out", "w")

item = {"1": 0, "i": 1, "j": 2, "k": 3}
prod = [["1", "i", "j", "k"], ["i", "-1", "k", "-j"], ["j", "-k", "-1", "i"], ["k", "j", "-i", "-1"]]

def product(a, b):
	result = prod[item[a]][item[b]]
	if len(result) > 1:
		return -1, result[1]
	return 1, result

# print product
cases = int(fin.readline().strip())
# print cases



for case in xrange(1, cases+1):
	answer = "Case #" + str(case) + ": "
	find_i = True
	find_j = True
	find_k = True
	mismatched = True

	l, x = [int(i) for i in fin.readline().strip().split()]

	string = fin.readline().strip()*x
	# print string

	if x*l > 2:
		operand = "1"
		pos = 1

		for index in xrange(x*l):
			sign, operand = product(operand, string[index])
			pos *= sign

			if find_i:
				if pos == 1 and operand == "i":
					find_i = False
					operand = "1"
					# print "Found i"
			elif find_j:
				if pos == 1 and operand == "j":
					find_j = False
					operand = "1"
					# print "Found j"
			elif find_k:
				if pos == 1 and operand == "k":
					find_k = False
					operand = "1"
					# print "Found k"

		if pos == 1 and operand == "1":
			mismatched = False				

	if find_i or find_k or find_j or mismatched:
		answer += "NO"
	else:
		answer += "YES"

	fout.write(answer + "\n")


fin.close()
fout.close()