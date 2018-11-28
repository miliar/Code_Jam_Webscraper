inp=file('A-small-attempt0.in').read().split('\n')
inp=inp[:len(inp)-1]
ot=open('out.txt','w')
n=int(inp[0])
c=0
for n1 in range(n):
	r1=int(inp[c+1])
	grd1=inp[c+2:c+6]
	r2=int(inp[c+6])
	grd2=inp[c+7:c+11]
	c+=10
	res1=map(int,grd1[r1-1].split())
	res2=map(int,grd2[r2-1].split())
	res=[]
	for r in res1:
		if r in res2:
			res.append(r)
	#print res
	if len(res)==1:
		print "Case #"+str(n1+1)+': '+str(res[0])
		ot.write("Case #"+str(n1+1)+': '+str(res[0])+'\n')
	elif len(res)>1:
		print "Case #"+str(n1+1)+': '+'Bad magician!'
		ot.write("Case #"+str(n1+1)+': '+'Bad magician!\n')
	else:
		print "Case #"+str(n1+1)+': '+'Volunteer cheated!'
		ot.write("Case #"+str(n1+1)+': '+'Volunteer cheated!\n')



ot.close()
		
