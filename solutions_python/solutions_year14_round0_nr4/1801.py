import sys
def Nstrat(N,K):
	scoreN=0
	N_l = [x for x in N]
	K_l = [x for x in K]
	while len(N_l)>0:
		if N_l[-1] > K_l[-1]:
			del N_l[-1]
			del K_l[0]
			scoreN = scoreN+1
		else:
			for k in range(len(K_l)):
				if K_l[k] > N_l[-1]:
					del K_l[k]
					break
			del N_l[-1]
	return scoreN
	
def Dstrat(N,K):
	scoreN=0
	N_l = [x for x in N]
	K_l = [x for x in K]
	while len(N_l)>0:
		index = None
		for i in range(len(N_l)):
			if N_l[i] > K_l[0]:
				index = i
				break
		if index != None:
			scoreN = scoreN+1
			del N_l[index]
			del K_l[0]
		else:
			del N_l[0]
			del K_l[0]
	return scoreN
				

sys.stdin = open('input.in','r')
sys.stdout = open('output.out','w+')
				
T = int(input())
for i in range(1,T+1):
	N = int(input())
	N = [float(x) for x in input().split()]
	K = [float(x) for x in input().split()]
	N.sort()
	K.sort()
	print('Case #{CaseNo}: {Dct} {Nrm}'.format(CaseNo=i,Dct=Dstrat(N,K),Nrm=Nstrat(N,K)))
	
sys.stdin = sys.__stdin__
sys.stdout = sys.__stdout__
