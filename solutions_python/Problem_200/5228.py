def findtidy(n):
	temp3 = 9
	temp = n
	con = False
	if( n % 10 == 0):
		n = n - 1
		con = True
	else:
		while(temp != 0):
			temp4 = int(temp % 10)
			if temp4 <= temp3:
				temp = int(temp / 10)
				temp3 = temp4
				continue
			else:
				con = True
				n = n - 1
				break
	while True:
		temp = n
		if(temp % 10 == 0):
			n = n - 1
			continue
		temp1 = 9
		con1 = True
		while(temp != 0):
			temp2 = int(temp % 10)
			if temp2 <= temp1:
				temp = int(temp / 10)
				temp1 = temp2
			else:
				con1 = False
				break
		if con1:
			break
		else:
			n = n - 1
	return n

fo = open("input11.in","r")
fo1 = open("output.txt","w")
i = int(fo.readline())
n = 1

while i:
	m = int(fo.readline())
	print(m)
	fo1.write("Case #")
	fo1.write('%s'%n)
	fo1.write(": ")
	if (m <= 9):
		fo1.write('%s'%m)
	else:
		tidy = findtidy(m)
		fo1.write('%s'%tidy)
	fo1.write("\n")
	n=n+1
	i=i-1
fo.close()
fo1.close()