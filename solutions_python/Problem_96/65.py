tests = input()
for i in range(1,tests+1):
	line = map(int,raw_input().split())
	N = line[0]
	S = line[1]
	p = line[2]
	points = line[3:]
	A = len(filter(lambda n: (n+2)/3>=p, points))
	B = len(filter(lambda n: (n+2)/3==(p-1) and ((n%3==0 and n/3>0) or (n%3==2)), points))
	solution = A+min(B,S)
	print "Case #"+str(i)+": "+str(solution)
