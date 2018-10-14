import sys

def solve(orig):
	N=orig-1
	NL = list(str(N))
	index = len(NL)-1
	while index > 0:
		while int(NL[index-1])>int(NL[index]):
			NL[index-1]=str(int(NL[index-1])-1)
		index -= 1
	sIndex = 0
	while sIndex < len(str(N)):
		while True:
			NLC = [i for i in NL]
			index = sIndex
			NLC[index] = str(int(NLC[index])+1)
			for i in range(index+1, len(str(N))):
				if int(NLC[i-1])>int(NLC[i]):
					NLC[i]=str(int(NLC[i])+1)
			if int("".join(NLC))>orig:
				break
			NL = NLC
		sIndex+=1
	return int("".join(NL))
				
inf = open(sys.argv[1],"r")
out = open(sys.argv[2], "w")
L = list(inf)
L = L[1:]
L = list(map(int, L))
case = 1
for input in L:
	out.write("Case #" + str(case)+": " + str(solve(input)) + "\n")
	case+=1