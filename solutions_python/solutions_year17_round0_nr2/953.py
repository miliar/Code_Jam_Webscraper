

def main(N):
	str_N = str(N)
	check = False
	list_N = list(str_N)
	temp = list(list_N[0])
	if len(list_N) == 1:
		return N
	for i in range(1,len(list_N)):
		if check:
			temp.append('9')
		else:
			if temp[-1]<=list_N[i]:
				temp.append(list_N[i])
			else:
				check = True
				dummy = int(temp[-1]+list_N[i])-1
				temp.pop(-1)
				if dummy ==9:
					temp.append("0")
				temp.append(str(dummy))
	N = int("".join(temp))
	if check:
		N = main(N)
	return N

T = input()
for i in range(T):
	t = input()
	print "Case #" + str(i+1) + ":",main(t)
