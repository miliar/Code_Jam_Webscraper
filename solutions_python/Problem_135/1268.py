#Codejam QR
#Problem A. Magic Trick
#Submitted By : Yogendra Tank

cases = input()
for case in range(cases):
	one = input()
	arr1=[[0 for x in xrange(5)] for x in xrange(5)]
	for num in range(4):
		arr1[num] = map(int,raw_input().split())
	two = input()	
	arr2=[[0 for x in xrange(5)] for x in xrange(5)]
	for num in range(4):
		arr2[num] = map(int, raw_input().split())
	
	flag = 0
	ans = 0
	for i in arr1[one-1]:
		if i in arr2[two-1]:
			flag+=1
			ans = i
	if flag == 1:print 'Case #'+str(case+1)+': '+str(ans)
	if flag > 1:print 'Case #'+str(case+1)+': Bad magician!'
	if flag == 0: print 'Case #'+str(case+1)+': Volunteer cheated!'