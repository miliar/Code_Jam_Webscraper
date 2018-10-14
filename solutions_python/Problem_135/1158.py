import sys
sys.stdin = open ('A-small-attempt0.in')
sys.stdout = open ('A.txt','w')

T = int(input().strip())
for z in range (T):
	r1 = int(input().strip())
	a1 = [[] for _ in range (4)]
	for i in range (4):
		a1[i]+=list(map(int,input().strip().split()))
	c1 = set(a1[r1-1])
	r2 = int(input().strip())
	a2 = [[] for _ in range (4)]
	for i in range (4):
		a2[i]+=list(map(int,input().strip().split()))
	c2 = set(a2[r2-1])
	overlap = list(c1&c2)
	if len(overlap)==0:
		print ('Case #{0}: Volunteer cheated!'.format(z+1))
	elif len(overlap)==1:
		print ('Case #{0}: {1}'.format(z+1,overlap[0]))
	else:
		print ('Case #{0}: Bad magician!'.format(z+1))
sys.stdout.close()