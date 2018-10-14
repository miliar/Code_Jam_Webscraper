count = int(input())
for i in range(count):
	n = input()
	n = list(map(lambda a: int(a), n))
	j = len(n)-1
	while j > 0:
		if int(n[j - 1]) > int(n[j]):
			for l in range(j,len(n)):
				n[l] = 9
			n[j - 1] = n[j - 1] - 1
		j -= 1
	m = "".join(map(str, n)).strip("0")
	print ("Case #"+str(i+1)+": "+m)
