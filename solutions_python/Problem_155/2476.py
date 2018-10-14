f=open('A-large.in','U')
fout=open('ans.txt','wb')
record=[line for line in f]
all=record[0]
qq=0
for rec in record[1:]:
	qq=qq+1
	(a,b)=rec.strip().split(' ')
	b=[int(ea) for ea in b]
	tot=0
	need=0
	i=0
	for aa in b:
		if tot<i and aa>0:
			need+=i-tot
			tot=i
		i=i+1
		tot=tot+aa
	fout.write('Case #'+str(qq)+': '+str(need)+'\n')