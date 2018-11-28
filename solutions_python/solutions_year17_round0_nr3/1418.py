from queue import Queue

cases = []


def treat(N,K):
	cases = []
	ocstalls = [0,N-1]
	spaces = [N-2]
	k = 0
	sortidstalls = range(len(ocstalls)-1)

	while k < K:
		# print("k is",k)
		for i in sortidstalls:
			if(k<K):
				k += 1
				r = int((ocstalls[i+1]+ocstalls[i])/2)
				ocstalls.append(r)
				
			if(k == K):
				L = max(r-ocstalls[i]-1,0)
				R = max(ocstalls[i+1]-r-1,0)
				y = max(L,R)
				z = min(L,R)
				return(str(y)+" "+str(z))
				
		ocstalls = sorted(ocstalls)
		# print("ocstalls",ocstalls)
		spaces = []
		# print("i",i)
		for c in range(len(ocstalls)-1):
			# print("space1",ocstalls[c+1]-ocstalls[c]-1)
			spaces.append(ocstalls[c+1]-ocstalls[c])

		# sortidstalls = [i[0] for i in sorted(enumerate(spaces), key=lambda x:x[1], reverse = True)]
		# or faster
		sortidstalls = sorted(range(len(spaces)),key=lambda x:spaces[x], reverse = True)
		
	





with open("C-small-2-attempt2.in", "r") as input:
	T = int(input.readline())
	for line in input:
		N,K = map(int, line.split())
		# print(N)
		# print(Order(N))
		cases.append(treat(N+2,K))





o = ""
for i in range(T):
	o += "Case #" + str(i+1) + ": " + str(cases[i]) + "\n"
# print(o)
	
with open("output2.txt", "w") as output:
	output.write(o)
