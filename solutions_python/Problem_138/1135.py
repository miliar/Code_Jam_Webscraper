def War (A, B, N):
	score = 0
	i = 0
	j = 0
	while i<N and j<N:
		c = 0
		while j<N and A[i]>B[j]:
			j += 1
			c += 1
		score += c
		i += 1
		j += 1
	return score
	
def DWar (A, B, N):
	i = 0
	j = 0
	score = 0
	# Fase 1 big removal
	while N>=1 and B[-1] > A[-1]:
		A.pop(0)
		B.pop()
		N = A.__len__()
        # Fase 2 lie with small
	while i<N  and j<N:
		while i<N and A[i]>B[j]:
			score += 1
			i += 1
			j += 1
		i += 1                
	return score
	
# Input data
infile = "D-large.in"
with open(infile, 'r') as f:
	data = f.read().split("\n")
while data[-1].isspace() or not(data[-1]):
	data.pop()
	
testCases = int(data[0])
dataL = data.__len__()

# Each case solution
c = 1 # Case iterator
WarScore = []
DWarScore = []
while c < dataL:
	N = int(data[c])
	NaoBlock = sorted([float(i) for i in data[c+1].split(" ")])
	KenBlock = sorted([float(i) for i in data[c+2].split(" ")])
	WarScore.append(War(NaoBlock, KenBlock, N))
	DWarScore.append(DWar(NaoBlock, KenBlock, N))
	c+=3
	
#Output data
outfile = "out.txt"
with open(outfile, 'w') as f:
	for i in range(testCases):
		f.write("Case #%i: %i %i\n" % (i+1, DWarScore[i], WarScore[i]))
			
