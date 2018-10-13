import fileinput
import sys

# format: python 1.py samples.txt answers.txt
filename=sys.argv[2]
open(filename,'w').close()
TestCases=0
RowChoice1=[]
row1data=[]
RowChoice2=[]
row2data=[]
filedata=[]
case3=0
for line in fileinput.input():
	filedata.append(line)
TestCases=int(filedata[0])
for i in range(1,len(filedata),10):
	RowChoice1.append(filedata[i])
for i in range(6,len(filedata),10):
	RowChoice2.append(filedata[i])
for i in range(2,len(filedata),10):
	row1data.append(filedata[i])
	row1data.append(filedata[i+1])
	row1data.append(filedata[i+2])
	row1data.append(filedata[i+3])
for i in range(7,len(filedata),10):
	row2data.append(filedata[i])
	row2data.append(filedata[i+1])
	row2data.append(filedata[i+2])
	row2data.append(filedata[i+3])

rowtest1=[]
rowtest2=[]

count1=0
count2=0
for i in range(TestCases):
	
	rowtest1=[]
	rowtest2=[]
	case3=0
	count1=0
	count2=0
	rowtest1.append((row1data[(int(RowChoice1[i]))+(i*4)-1].split(' ')[0]).strip())
	rowtest1.append((row1data[(int(RowChoice1[i]))+(i*4)-1].split(' ')[1]).strip())
	rowtest1.append((row1data[(int(RowChoice1[i]))+(i*4)-1].split(' ')[2]).strip())
	rowtest1.append((row1data[(int(RowChoice1[i]))+(i*4)-1].split(' ')[3]).strip())

	rowtest2.append((row2data[(int(RowChoice2[i]))+(i*4)-1].split(' ')[0]).strip())
	rowtest2.append((row2data[(int(RowChoice2[i]))+(i*4)-1].split(' ')[1]).strip())
	rowtest2.append((row2data[(int(RowChoice2[i]))+(i*4)-1].split(' ')[2]).strip())
	rowtest2.append((row2data[(int(RowChoice2[i]))+(i*4)-1].split(' ')[3]).strip())

	for j in range(4):
			for k in range(4):
				if rowtest1[j]==rowtest2[k]:
				     # case 2
				     if case3==2:
					print 'Case #'+str(i+1)+': Bad magician!'
					towrite=open(filename,'a')
					towrite.write('Case #'+str(i+1)+': Bad magician!\n')
					towrite.close()	
					case3=1
					break	
				     #case1
				     else:			
					case3=2
					count1=i
					count2=j
			if case3==1:
				break
	if case3==2:
			print 'Case #'+str(count1+1)+': '+rowtest1[count2] 
			towrite=open(filename,'a')
			towrite.write('Case #'+str(count1+1)+': '+rowtest1[count2]+'\n' )
			towrite.close()
					

	#case 3
	if case3==0:
			print 'Case #'+str(i+1)+': Volunteer cheated!'
			towrite=open(filename,'a')
			towrite.write('Case #'+str(i+1)+': Volunteer cheated!\n')
			towrite.close()
					

		
		

