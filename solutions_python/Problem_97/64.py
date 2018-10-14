def shifts(number):
	n = str(number)
	res = []
	for i in range(1,len(n)):
		res.append(int(n[i:]+n[:i]))
	return res

tests = input()
for ii in range(1,tests+1):
	[a,b] = map(int,raw_input().split())
	solution = 0
	for i in range(a+1,b+1):
		pairs = list(set(shifts(i)))
		solution += len(filter(lambda x:x<i and x>=a,pairs))
			
	print "Case #"+str(ii)+": "+str(solution)
