def isTidy(num):
	num = str(num)
	for x in range(1,len(num)):
		if num[x-1] > num[x]:
			return False

	return True


cases = int(raw_input())
for h in range(cases):
	values = raw_input()
	top = values
	index = 0
	while not isTidy(int(values)):
		outerbreak = False
		for x in range(len(values)):
			while int(values[x])> int(values[x+1]):
				a = int(values[x])
				b = "9"*len(values[x+1:])
				values = values[0:x]+str(a-1)+b
				outerbreak = True
				break
			if outerbreak:
				break
	print("Case #{0}: {1}".format(h+1,int(values)))