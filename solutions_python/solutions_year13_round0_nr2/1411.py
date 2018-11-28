import sys
#import math
def Blawnmower(InputFileName):
	OutputFileName=InputFileName.replace('.in','.out')
	f1=open(InputFileName)
	#lines = open(InputFileName).read().splitlines()???
	f2 = open(OutputFileName,'w')
	T=int(f1.readline())
	for t in range(1,T+1):
		[N,M]=map(int, f1.readline().split())
		#N=int(N);M=int(N)???
		MtrxLawn=[map(int, f1.readline().split()) for k in range(N)]
		result='YES'
		for n in range(N):
			if result=='NO': break
			for m in range(M):
				if len([x for x in MtrxLawn[n][:] if x>MtrxLawn[n][m]])>0 \
				and len([x for x in zip(*MtrxLawn)[:][m] if x>MtrxLawn[n][m]]):
					result='NO';break						
		# if MtrxLawn in AllLawns(N,M): result='YES'
		# else: result='NO'
		f2.write('Case #'+str(t)+': ' + str(result)+'\n')#, file=f)
# def AllLawns(N,M):
	# MtrxTemp=[[2 for i in range(M)] for j in range(N)]
	# MtrxTemp.append([[1 for i in range(M)] for j in range(N)])
	# for n in range(N):
		# MtrxTemp.append(MtrxTemp[0][i][j])?!
	# for m in range(M):
	# print MtrxTemp
	# return MtrxTemp
def main():	
	if len(sys.argv)==2: FileName=sys.argv[1]
	else: FileName='B-example.in'
	Blawnmower(FileName)
if __name__ == '__main__':
	main()