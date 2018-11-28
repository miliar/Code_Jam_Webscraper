import sys
fopen=open('/Users/subodhyadav/Desktop/A-small-attempt0.in-2.txt','r')
fout=open('/Users/subodhyadav/Desktop/B-large.out.txt','a')
for k in xrange(int(fopen.readline().strip())):
	n=int(fopen.readline().strip())
	l=[]
	for i in xrange(n):
		l1=fopen.readline().strip()
		l.append(l1)
	r=[]
	r.append([l[0][0],0,0])
	count=0
	for i in l[0]:
		if r[-1][0]!=i:
			r.append([i,1,1])
		else:
			r[-1][1]+=1
			r[-1][2]+=1
	for i in l[1:]:
		ct,cc,flag=0,0,0
		for j in i:
			while 1:
				if ct>=len(r) and flag==0:
					count="Fegla Won"
					break
				if j!=r[ct][0] and flag==0:
					count="Fegla Won"
					break
				elif j==r[ct][0] and flag==0:
					flag=1
					cc=1
					break
				elif j==r[ct][0] and flag==1:
					cc+=1
					break
				elif j!=r[ct][0] and flag==1:
					if cc>r[ct][2]:
						r[ct][2]=cc
					elif cc<r[ct][1]:
						r[ct][1]=cc
					ct+=1
					cc=0
					flag=0
			if count=="Fegla Won":
				break
		if ct<len(r)-1:
			count="Fegla Won"
		if count=="Fegla Won":
			break
		if cc>r[ct][2]:
			r[ct][2]=cc
		elif cc<r[ct][1]:
			r[ct][1]=cc		
	if count!="Fegla Won":
		for i in r:
			count+=i[2]-i[1]
	fout.write("Case #")
	fout.write(str(k+1))
	fout.write(": ")
	fout.write(str(count))
	fout.write("\n")
fout.close()
fopen.close()