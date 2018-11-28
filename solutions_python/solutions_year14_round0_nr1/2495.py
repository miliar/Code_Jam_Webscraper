t=input()
case=1
while t!=0:
	a=input()
	x=[]
	y=[]
	for i in range(0,4):
		s=raw_input().split()
		for j in range(0,4):
			s[j]=int(s[j])
		x.append(s)
	b=input()
	for i in range(0,4):
		s=raw_input().split()
		for j in range(0,4):
			s[j]=int(s[j])
		y.append(s)
	m=17*[0]
	for i in range(0,4):
		m[x[a-1][i]]+=1
	ind=-1
	cnt=0
	for i in range(0,4):
		if m[y[b-1][i]]==1:
			cnt+=1
			ind=i
	if cnt==0:
		print "Case #%d"%case+": Volunteer cheated!"
	if cnt==1:
		print "Case #%d"%case+": %d"%y[b-1][ind]
	if cnt>1:
		print "Case #%d"%case+": Bad magician!"
	case+=1
	t-=1


