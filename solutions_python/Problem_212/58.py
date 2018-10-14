getline = lambda: [int(x) for x in raw_input().split()]

T = int(raw_input())
for test_case in range(T):
	N, P = getline()
	G = getline()
	countmod = lambda G, P, i: len([x for x in G if x%P == i])
	cm = [countmod(G,P,i) for i in range(P)]
	if P == 2:
		answer = cm[0] + (cm[1]+1)/2
	if P == 3:
		a,b = sorted([cm[1], cm[2]])
		answer = cm[0] + a + (b-a+2)/3
	if P == 4:
		a,b = sorted([cm[1], cm[3]])
		if cm[2]%2 == 0:
			end = (b-a+3)/4
		else:
			end = 1 + (b-a+1)/4
		answer = cm[0] + cm[2]/2 + a + end 
	print "Case #%s: %s"%(test_case+1, answer)
