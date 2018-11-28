t = int(raw_input())
for i in range(t):
	line = raw_input().split()
	n = int(line[0])
	s = int(line[1])
	p = int(line[2])
	data = line[3:]
	for j in range(len(data)):
		data[j]=int(data[j])
	data=sorted(data)[::-1]
	count=0
	for j in data:
		if j/3>=p:
			count+=1
		elif p-1>=0 and (j-1)/3>=p-1:
			count+=1
		else :
			if s==0:	
				break
			elif p-2>=0 and (j-2)/3>=p-2:
				count+=1
				s-=1
	print 'Case #'+str(i+1)+':',count

