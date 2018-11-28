fo = open("out","w")
tc=input()
for i in xrange(1,tc+1):
	answer="Volunteer cheated!"
	r1=input()
	for x in xrange(1,5):
		if x==r1:
			a1=map(int,raw_input().split())
		else:
			raw_input()
	r2=input()
	for x in xrange(1,5):
		if x==r2:
			a2=map(int,raw_input().split())
		else:
			raw_input()
	y=set(a1) & set(a2)
	if len(y)==1:
		answer=y.pop()
	elif len(y)>1:
		answer="Bad magician!"
	fo.write("Case #"+str(i)+": "+str(answer)+"\n")
fo.close()