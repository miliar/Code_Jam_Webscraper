
def get_ans(line):
	ck = line.split(" ")[0]
	K = int(line.split(" ")[1])

	cnt = 0
	ck = [ c for c in ck]

	for i in range(len(ck)-K+1):

		if ("".join(ck)).find("-") == -1:
			break

		if ck[i] == "-":
			cnt += 1

			for j in range(i, i+K):
				if ck[j] == "+" : ck[j] = "-"
				elif ck[j] == "-" : ck[j] = "+"

		# print "".join(ck)


	if ("".join(ck)).find("-") != -1:
		return "IMPOSSIBLE"

	return cnt


fname = "ip.txt"
fname = "A-small-attempt0.in"
fname = "A-large.in"

f = open(fname,"r")

lines = f.readlines()

total = int(lines[0])
for i in range(total):
	s = lines[i+1].split("\n")[0]

	ans = get_ans(s)

	ans = "Case #"+str(i+1)+": "+ str(ans)
	print ans