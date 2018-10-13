import sys
sys.stdin = open('input.in','r')
sys.stdout = open('output.out','w+')

def f(C,F,X, n):
	res = 0
	for i in range(n):
		res = res+ C/(2+i*F)
	res = res + X/(2+n*F)
	return res

T = int(input())
for i in range(1,T+1):
	[C,F,X] = [float(d) for d in input().split()]
	n = ((F*X - 2*C)/(C*F))-1
	if n<0:
		n=-1
	res = f(C,F,X, int(n)+1)
	print('Case #{CaseNo}: {Res}'.format(CaseNo=i,Res=res))
	
sys.stdin = sys.__stdin__
sys.stdout = sys.__stdout__