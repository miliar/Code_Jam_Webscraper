def fun(l1,l2):
	if ((l1 == []) or (l2 == [])):
		return 0
	elif (l1[1] == l2[1]):
		a = l1[2:]
		b = l2[2:]
		if(l1[0] < l2[0]):
			l2[0] = l2[0] - l1[0]
			return l1[0] + fun(a,l2)
		elif(l1[0] > l2[0]):
			l1[0] = l1[0] - l2[0]
			return l2[0] + fun(l1,b)
		else:
			return l1[0] + fun(a,b)
	else:
		a = l1[2:]
		b = l2[2:]
		return max(fun(a,l2),fun(l1,b))
		
a = raw_input()
a = int(a)

i = 0
while i < a:
	result = "Case #" + str(i+1) + ": "
	b = raw_input()
	c = raw_input()
	d = raw_input()
	c = c.split(" ")
	d = d.split(" ")
	c = map(int , c)
	d = map(int , d)
	res = str(fun(c,d))
	result = result + res
	print result
	i = i + 1
