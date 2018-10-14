badmag="Bad magician!"
volcht="Volunteer cheated!"
result=""

file = open('A-small-attempt0.in')
output = open('output1.txt','w')
lines=int(float(file.readline()))

for x in range(0,lines):
	row1 = int(file.readline().strip())
	ctr=1
	cards=[]
	while(ctr<=4):
		if(row1==ctr):
			cards=file.readline().strip().split()
		else:
			file.readline()
		ctr=ctr+1
	row2 = int(file.readline().strip())
	ctr=1
	cards2=[]
	while(ctr<=4):
		if(row2==ctr):
			cards2=file.readline().strip().split()
			resctr=0
			for c in cards:
				if(c in cards2):
					result=str(c)
					resctr=resctr+1
					if(resctr>1):
						result=badmag
						break
			if resctr==0:
				result=volcht
		else:
			file.readline()
		ctr=ctr+1



	# print result
	output.write('Case #'+str(x+1)+': ')
	output.write(str(result))
	output.write('\n')
