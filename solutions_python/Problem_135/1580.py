##jkmfd=raw_input()
t=int(raw_input())
for i in range(0,t):
	p1=raw_input()
	r1=[raw_input().split() for x in range(0,4)]
	p2= raw_input()
	r2=[raw_input().split() for x in range(0,4)]
	arr1=r1[int(p1)-1]
	arr2=r2[int(p2)-1]
	interset=[val for val in arr1 if val in arr2]
	if len(interset)==1:
    		a=interset[0]
    		print 'Case #'+str(i+1)+': '+a
	elif len(interset)>1:
    		print 'Case #'+str(i+1)+': '+'Bad magician!'
	else:
    		print 'Case #'+str(i+1)+': '+'Volunteer cheated!'


