def CountFlips(S):
	Stek = S[0]
	n = len(Stek)
	num = S[1]
	count = 0
	for i in range(len(Stek)):
		#print Stek
		if Stek[i] == 0:
			if (n-i < num):
				return 'IMPOSSIBLE'
			else:
				for j in range(num):
					Stek[i+j]^=1
				count +=1
	return str(count)

with open('/Users/gorankovacevic/Desktop/D&A of Algos/Google/Code Jam Practice/Flips/A-large.txt') as f:
	a = []
	for line in f:
		a.append(line)
		
fout = open('/Users/gorankovacevic/Desktop/D&A of Algos/Google/Code Jam Practice/Flips/A-largeOut.txt', 'w')
		
N = int(a[0][0])
case = 1
#print a

test = 0
A = []
for i in range(1,len(a)):
	pom = []
	pom1 = []
	pom2 = ''
	for j in range(len(a[i])):
		if a[i][j] == '\n':
			break
		if a[i][j] ==' ':
			test = 1
			pom.append(pom1)
			continue
		if test == 0:
			if a[i][j] == '+':
				pom1.append(1)
			else:
				pom1.append(0)
		else:
			pom2+=a[i][j]
	pom.append(int(pom2))
	A.append(pom)
	test = 0
	
#print A

for i in range(len(A)):
	out = CountFlips(A[i])
	out+='\n'
	fout.write("Case #" + str(case) + ": " + out)
	case += 1
