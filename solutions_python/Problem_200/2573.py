with open("input.txt","r") as f:
	data = f.read().split("\n")

def tidy(n):
	n = list(str(n))
	return sorted(n) == n

output = ""
case = 1
while case < len(data):
	N = int(data[case])
	if tidy(N):
		answer = N
	else:
		l = list(str(N))
		i = 0
		while i < len(l)-1:
			if l[i] > l[i+1]:
				N = N - int("".join(l[i+1:])) -1
				l = list(str(N))
				if tidy(N):
					answer = N
					break
				else:
					i = 0
			else:
				i+=1

	output += "Case #{}: {}\n".format(case,answer)
	case+=1
print(output)
with open("output.txt","w+") as f:
	f.write(output[:-1])

