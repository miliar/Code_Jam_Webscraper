fin=open('A-small.in','r')
fout=open('A-small.out','w')
T=int(fin.readline())
for I in range(1,T+1):
	fout.write('Case #'+str(I)+': ')
	r=int(fin.readline())
	firstCase=[]
	for i in range(1,5):
		a=fin.readline()
		if r==i: firstCase=a.split()
	
	r=int(fin.readline())
	col=0
	card='2'
	for i in range(1,5):
		a=fin.readline()
		if r==i:
			for c1 in firstCase:
				for c2 in a.split():
					if c1==c2: 
						print(c1,c2)
						col+=1
						card=c1
	ans=""
	if col==1: ans=card
	elif col==0: ans="Volunteer cheated!"
	else: ans="Bad magician!"
	fout.write(ans+'\n')	