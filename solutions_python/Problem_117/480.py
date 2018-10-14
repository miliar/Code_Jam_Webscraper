
import numpy as np

def readInput(filename):
	fid = open(filename, 'r')
	T = int(fid.readline())
	R = []
	for zzz in range(0,T):
		#print '****************'
		#line = fid.readline().rstrip('\n').split()
		line = fid.readline().rstrip('\n').split()
		N = int(line[0])
		M = int(line[1])
		D = np.zeros((N,M), dtype=np.int)
		for qqq in range(0,N):
			line = fid.readline().rstrip('\n').split()
			D[qqq] = line
		#print D
		solution = checkMat(D,N,M)
		#when solution is obtained do 
		R.append(solution)
	
	print R
	fileOut = filename[0:-2] + 'out'
	writeSolution(R,fileOut)


def checkMat(Ori,N,M):
	maxH = np.max(Ori)
	minH = np.min(Ori)
	if maxH == minH:
		return 'YES' 
	else:
		for i in range(0,N):
			for j in range(0,M):
				maxR = max(Ori[i,:])
				maxC = max(Ori[:,j])
				val = Ori[i,j]
				#print "* ",val,maxR,maxC
				if (maxR > val) and (maxC > val):
					return 'NO'
				#print val
				#print sum(Ori[i,:])
				#print M,N
				#if (sum(Ori[i,:]) != M) and (sum(Ori[:,j]) != N):
				#	return 'NO'
		return 'YES'
	

def writeSolution(R,filename):
	idx = 1
	fid = open(filename,'w')
	for line in R:
		h = 'Case #' + str(idx) + ': ' 
		hh = h + ''.join(str(line)) + '\n'
		fid.write(hh)
		idx += 1
	fid.close()



#D=readInput('B.in')
#D=readInput('B-small-attempt1.in')
D=readInput('B-large.in')


