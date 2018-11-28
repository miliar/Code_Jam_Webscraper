d={}
#COnfirm
d[(2,1,2)]=1
d[(2,1,4)]=1
d[(2,2,2)]=1
d[(2,2,3)]=1
d[(2,2,4)]=1
d[(2,3,4)]=1
d[(2,4,4)]=1

d[(3,1,3)]=0
d[(3,2,3)]=1
d[(3,3,3)]=1
d[(3,3,4)]=1

d[(4,4,1)]=0
d[(4,2,4)]=0

d[(4,3,4)]=1
d[(4,4,4)]=1


for x in range(1,5):
	for r in range(1,5):
		for c in range(1,5):
			if (x==1):
				d[(x,r,c)]=1
			elif (x>max(r,c)):
				d[(x,r,c)]=0
			if (r*c)%x!=0:
				d[(x,r,c)]=0
			else:
				if (x,r,c) not in d:
					if (x,c,r) in d:
						d[(x,r,c)]=d[(x,c,r)]
					else:
						print x,r,c

for x in d:
	if (d[x]!=d[(x[0],x[2],x[1])]):
		print x
t=input()
tt=1
while tt<=t:
	x,r,c=map(int,raw_input().split())
	if d[(x,r,c)]:
		print "Case #"+str(tt)+": GABRIEL"
	else:
		print "Case #"+str(tt)+": RICHARD"
	tt+=1