with open("input.txt","r") as f:
	data = f.read().split("\n")

def flip(L,start,n):
	i = 0
	while i < n:
		L[i+start] = not L[i+start]
		i+=1
	return L

output = ""
case = 1
while case < len(data):
	thisData = data[case].split(" ")
	S = [char == "+" for char in thisData[0]]
	#print(case)
	k = int(thisData[1])
	#print(S,k)
	pos = 0
	flips = 0
	while pos < (len(S)-k)+1:
		if S[pos] is False:
			S = flip(S,pos,k)
			#print(S)
			flips += 1
		else:
			pos+=1
	if all(S):
		answer = flips
	else:
		answer = "IMPOSSIBLE"
	output += "Case #{}: {}\n".format(case,answer)
	case+=1
#print(output)
with open("output.txt","w+") as f:
	f.write(output[:-1])

