t=int(raw_input())
for x in xrange(1,t+1):
	no1=int(raw_input())
	t1=[[],[],[],[],[]]
	for temp in xrange(1,5):
		t1[temp]=map(int,raw_input().split())

	no2=int(raw_input())
	t2=[[],[],[],[],[]]
	for temp in xrange(1,5):
		t2[temp]=map(int,raw_input().split())
	count=0
	val=0
	for ss1 in t1[no1]:
		for ss2 in t2[no2]:
			if ss1==ss2:
				count+=1
				val=ss1
	if count==0:
		ans="Volunteer cheated!"
	elif count==1:
		ans=val
	else:
		ans="Bad magician!"
	print "Case #%s: %s"%(x,ans)