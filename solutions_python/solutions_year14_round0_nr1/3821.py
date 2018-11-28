fin=file('a');
fout=file('MagicOutput.txt','w');

a=[]
b=[]
c=[]
data=[]
no=[];
for x in range(1,17):
	data.append(False);

no_test=int(fin.readline())
for x in range(0,no_test):
	data=[];
	for z in range(1,17):
		data.append(False);
	no=[]
	a=[]
	b=[]
	row_1=int(fin.readline())-1
	for y in range(0,4):
		a.append(fin.readline().split());
	row_2=int(fin.readline())-1
	for y in range(0,4):
		b.append(fin.readline().split());
	for e in a[row_1]:
		data[int(e)-1]=True;
	for e in b[row_2]:
		if(data[int(e)-1]):
			no.append(e)
	if(len(no)>1):
		fout.write("Case #%s: Bad magician!\n"%(x+1))
	elif(len(no)==0):
		fout.write("Case #%s: Volunteer cheated!\n"%(x+1))
	elif(len(no)==1):
		fout.write("Case #%s: %s\n"%((x+1),no[0]))
	
	

