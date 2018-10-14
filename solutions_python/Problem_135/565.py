import sys
sys.stdin = open('input.in','r')
sys.stdout = open('output.out','w+')

T = int(input())
for i in range(1,T+1):
	ans_1 = int(input())
	grid_1 = [[int(x) for x in input().split()] for j in range(4)]
	ans_2 = int(input())
	grid_2 = [[int(x) for x in input().split()] for j in range(4)]
	r_1 = grid_1[ans_1-1]
	r_2 = grid_2[ans_2-1]
	c = 0
	res = 0
	for v in r_1:
		if v in r_2:
			res = str(v)
			c = c+1
	if c==0:
		res = 'Volunteer cheated!'
	elif c>1:
		res = str('Bad magician!')
	else:
		pass
	print('Case #{CaseNo}: {Res}'.format(CaseNo=i,Res=res))
	
sys.stdin = sys.__stdin__
sys.stdout = sys.__stdout__