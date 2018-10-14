T = int(input())
for t in range(T):
#	print("Case #" + str(t+1), end=": ")
	line = input().split()
	N = int(line[0])
	S = int(line[1])
	p = int(line[2])
	if p == 0:
		nmin = 0
	elif p == 1:
		nmin = 1
		pmin = 1
	else:
		nmin = p*3 -2
		pmin = nmin -2 
	result = 0
	for x in line[3:]:
		if int(x) >= nmin:
			result += 1
		elif S > 0 and int(x)>=pmin:
			S -= 1
			result += 1
	print("Case #" + str(t+1) + ": " + str(result))
