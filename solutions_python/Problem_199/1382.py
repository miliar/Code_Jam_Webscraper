Ss = []
times = 0
cases = []
with open("A-large.in", "r") as input:
	T = int(input.readline())
	for line in input:
		S,K = line.split()
		K = int(K)
		# print(S,K)
		Ss = [0 if s=='+' else 1 for s in S]
		l = len(Ss)
		# print(l-K+1)
		times = 0
		for i in range(l-K+1):
			if Ss[i] == 1:
				# print(Ss, Ss[i:i+K], i)
				Ss[i:i+K] = [(1 if s==0 else 0) for s in Ss[i:i+K]]
				# print(Ss[i:i+K])
				times += 1
		impossible = 0
		for i in range(l-K+1, l):
			if Ss[i] == 1:
				impossible = 1
				
		# print(Ss,times, impossible)
		case = times if impossible == 0 else "IMPOSSIBLE"
		cases.append(case)
o = ""
for i in range(T):
	o += "Case #" + str(i+1) + ": " + str(cases[i]) + "\n"
# print(o)
	
with open("output.txt", "w") as output:
	output.write(o)
	