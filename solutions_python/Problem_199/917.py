def main(string,k):
	list_S = list(string)
	cnt = 0
	sol = ['+']*len(list_S)
	for i in range(len(list_S)-k+1):
		if list_S[i] == "-":
			cnt+=1
			for j in range(k):
				if list_S[i+j] == "+":
					list_S[i+j] = "-"
				else:
					list_S[i+j] = "+"
	if list_S == sol:
		return cnt
	return "IMPOSSIBLE"


T = input()
for i in range(T):
	data = raw_input().split()
	print "Case #"+str(i+1)+":",main(data[0],int(data[1]))
