t = int(input())
for i in range(1, t + 1):
	o = input()
	done = False
	num = list(o)
	n = list(o)
	tam = len(n)
	ans = ''
	isNum = False
	for x in range(tam-1):
		p = 10**(tam-1-x)
		q = p*int(n[x])
		minimum = int(n[x]*len(str(p)))
		if int(''.join(num))< minimum:
			isNum = True
			break
		else:
			ans = ans + n[x]
			num.pop(0)
			isNum = False
	if isNum == True:
		print("Case #{}: {}".format(i, ans+str(q-1)))
	else:
		print("Case #{}: {}".format(i, o))