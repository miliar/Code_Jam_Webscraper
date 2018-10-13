f = open('A-large.in', 'r')
g = open('Case1soln.dat', 'w')
g.close()
g = open('Case1soln.dat', 'a')
NumCases=int(f.readline())
for i in range (2,NumCases+2):
	line=f.readline().rstrip()
	words=line.split(' ')
	NumSteps=int(words[0])
	Table1=[]
	Table2=[]
	Table3=[]
	for j in range (1,2*NumSteps+1):
		#print words[j]
		if j%2==1:
			Table1.append(int(words[j+1]))
			if words[j]=='O':
				Table2.append((j+1)/2-1)
			else:
				Table3.append((j+1)/2-1)

#	print Table1
#	print Table2
#	print Table3
	Table2.append(101)
	Table3.append(101)
	time=0
	O=1
	B=1
	pop2=0
	pop3=0
	while time<100000000:
		time=time+1;


		if Table2[0]<Table3[0] and Table1[Table2[0]]==O:			
			Table2.pop(0)
			pop2=1
		elif Table3[0]<Table2[0] and Table1[Table3[0]]==B:
			Table3.pop(0)			
			pop3=1
		elif Table3[0]==Table2[0]:
			break

		if pop2==0:
			if Table2[0]!=101:
				if O<Table1[Table2[0]]:
					O=O+1
				elif O>Table1[Table2[0]]:
					O=O-1
		else:
			pop2=0

		if pop3==0:
			if Table3[0]!=101:		
				if B<Table1[Table3[0]]:
					B=B+1
				elif B>Table1[Table3[0]]:
					B=B-1
		else:
			pop3=0
	
	g.write('Case #' + str(i-1) + ': ' + str(time-1) + '\n')




