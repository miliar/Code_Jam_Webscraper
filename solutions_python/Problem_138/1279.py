fopen = open('D-large.in')
fopen2 = open('Output.txt','w')
T = fopen.readline().strip()
T = int(T)
for num in range(1,T+1):
	dwar = 0
	nwar = 0
	len = int(fopen.readline().strip())
	line1 = fopen.readline()
	line2 = fopen.readline()
	l1 = line1.strip().split(" ")
	l2 = line2.strip().split(" ")
	l3 = line1.strip().split(" ")
	l4 = line2.strip().split(" ")
	for a in range(0,len):
		l1.sort()
		l2.sort()
		flag = 0
		for n in l2:
			if n > l1[0]:
				l2.remove(n)
				flag = 1
				break
		if flag == 0:
			l2.pop(0)
			nwar += 1
		l1.pop(0)
	for a in range(0,len):
		l3.sort()
		l4.sort()
		flag = 0
		for n in l3:
			if n < l4[0]:
				l4.pop(len-a-1)
				l3.remove(n)
				flag = 1
				break
		if flag == 0:
			if l3[0] > l4[0]:
				dwar+=1
			l3.pop(0)
			l4.pop(0)
	output="Case #" + str(num) + ": " + str(dwar) + " " + str(nwar)
	fopen2.write(output+"\n")
fopen2.close()
fopen.close()