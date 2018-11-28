array = []
pc = 0
f = 0
j = 0

t = int(input())

for i in range(1,t+1):
	array = []
	pc = 0
	f = 0
	j = 0

	p,k = [str(x) for x in input().split(" ")]
	k = int(k)

	for a in range(0,len(p)): #totals
		array.append(p[a])
		if p[a] == "+":
			pc = pc+1

	if pc == len(p): #all happy sided
		print("Case #{}: 0".format(i))

	else:
		for q in range(0, len(array)):
			if array[q] == "+":
				pass
			if array[q] == "-":
				try:
					for w in range(q,q+k):
						if array[w] == "-":
							array[w] = "+"
						else:
							array[w] = "-"
					f = f+1
				except IndexError:
					print("Case #{}: {}".format(i,"IMPOSSIBLE"))
					j = 1
					break
		if j == 0:
			print("Case #{}: {}".format(i,f))
