def is_pretty(line):
	num = int(line)
	sp = []
	while (num):
		rem = num%10
		num=num/10
		sp.append(rem)
	sp.reverse()
	for i in range(0,len(sp)):
		if (i+1) < len(sp):
			if sp[i+1] < sp[i]:
				return False
	return True

def make_pretty(line):
	
	if is_pretty(line):
		return str(int(line))
	
	num = int(line)
	orig =num
	flag = True
	sp = []
	while (num):
		rem = num%10
		num=num/10
		sp.append(rem)
	sp.reverse()
	point =len(sp)-1
	for i in range(0,len(sp)):
		if (i+1) < len(sp):
			if sp[i+1] < sp[i]:
				if sp[i] ==0:
					sp[i] =9
				else:
					sp[i] = sp[i]-1
				point =i+1
				break
	for i in range(point, len(sp)):
		sp[i] =9
	output = ''.join(map(str,sp))
	output = output.lstrip('0') 
	
	if is_pretty(output):
		return output
	else:
		return make_pretty(output)

fileName = 'B-large.in'
fileHandle =open(fileName, 'r')
firstLine = fileHandle.readline().rstrip()
numTests = int(firstLine)
k=1
for line in fileHandle:
	num = make_pretty(line)
	print "Case #"+str(k)+": "+ num
	k=k+1


