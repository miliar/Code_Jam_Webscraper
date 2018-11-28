
T = int(raw_input())
for t in  xrange(T): 
	ans1 = int(raw_input())
	mat1 = []
	for m in xrange(4):
		mat1.append(map(int,raw_input().split()))
	#print mat1
	
	ans2 = int(raw_input())
	mat2 = []
	for m in xrange(4):
		mat2.append(map(int,raw_input().split()))
	#print mat2
	
	s = set(mat1[ans1-1]).intersection(set(mat2[ans2-1]))
	#print s, len(s)

	ans = "Case #"+str(t+1)+": "
	if len(s) == 0 : 
		print ans+"Volunteer cheated!"
	elif len(s) == 1 : 
		print ans+str(s.pop())
	else :
		print ans+"Bad magician!"

