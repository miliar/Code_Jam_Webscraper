import sys
#sys.stdin = open('A-small-attempt0.in', 'r')
#sys.stdout = open('A.out','w')

T = int(input())
for p in range(T):
	n = int(input())
	g1 = []
	for i in range(4):
		w = list(map(int,input().split()))
		if i == n-1:
			g1 = w 
	m = int(input())
	g2 = []
	for i in range(4):
		w = list(map(int,input().split()))
		if i == m-1:
			g2 = w
	y = set(g1) & set(g2)
	#print(g1, g2, y)
	if len(y) > 1:
		print("Case #%d: %s" % (p+1, 'Bad magician!'))
	else:
		if len(y) == 1:
			print("Case #%d: %d" % (p+1, y.pop()))
		else:
			print("Case #%d: %s" % (p+1, 'Volunteer cheated!'))
	

	
