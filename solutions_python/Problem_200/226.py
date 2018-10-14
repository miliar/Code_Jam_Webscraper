fin = open("B-large.in",'r')
f = open("B.out",'w')

tt = int(fin.readline())

for t in xrange(tt):
	digitstrs = [c for c in fin.readline()]
	digits = []
	for c in digitstrs:
		try:
			digits.append(int(c))
		except:
			pass
	max_val,carry = digits[-1],len(digits)
	result = []
	for i in xrange(len(digits)):
		if digits[-1-i]<max_val:
			max_val = digits[-1-i]
		elif digits[-1-i]>max_val:
			carry = len(digits)-i-1
			max_val = digits[-1-i]-1
	for i in xrange(len(digits)):
		if i<carry:
			result.append(str(digits[i]))
		elif i==carry:
			result.append(str(digits[i]-1))
		else:
			result.append('9')
	f.write("Case #{0}: {1}\n".format(t+1,int("".join(result))))
f.close()
