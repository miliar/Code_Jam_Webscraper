import collections
compare = lambda x, y: collections.Counter(x) == collections.Counter(y)

file_in = open("B.in", "r")
file_out = open("B-small.out", "w")

def output (string):
	file_out.write(string + "\n")
	print(string)

case = 1
read = 0
A = 0
B = 0
K = 0
for number, line in enumerate(list(file_in)):
	if number == 0:
		continue
	A, B, K = line[:-1].split()
	chnce = 0
	for a in range(int(A)):
		for b in range(int(B)):
			if a & b < int(K):
				chnce += 1
	output("Case #{}: ".format(case) + str(chnce))
	case += 1

file_in.close()
file_out.close()