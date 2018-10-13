a=raw_input()
itr1=[]
itr2=[]

arr1=[]
arr2=[]
inp1=[]
inp2=[]
for i in range(0,int(a)):
	b=raw_input()
	inp1.append(b)
	for j in range(0,4):
		nos=raw_input()
		arr1.append(nos)
	c=raw_input()
	inp2.append(c)
	for j in range(0,4):
		nos=raw_input()
		arr2.append(nos)

for i in range(0,int(a)):
	temp1=arr1[int(inp1[i])-1+i*4]
	temp2=arr2[int(inp2[i])-1+i*4]
	xx=temp1.split(' ')
	yy=temp2.split( ' ')
	ct=0
	no=''
	for a in xx:
		if(a in yy):
			no=a
			ct+=1
	# print ct
	strt="Case #"+str(i+1)+":"
	if(ct==1):
		print strt,no	
	if(ct > 1):
		print strt,"Bad magician!"
	if(ct ==0):
		print strt,"Volunteer cheated!"	