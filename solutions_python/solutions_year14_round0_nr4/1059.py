f = open('D-large.in', 'r')
numTest = int(f.readline())
print numTest

fAns = open('ansQ4.txt', 'w')
def findFirstIndexGreater(v, newN):
	for i,n in enumerate(newN):
		if n > v:
			return i
	return 0
def War(K, N, num):
	newK = list(K)
	newN = list(N)
	point = 0
	for k in newK:
		ind = findFirstIndexGreater(k, newN)
		if newN[ind] < k:
			point += 1
		del newN[ind]
	return point
def allPossiblePair(K, N, num):
	r = []
	for k in K:
		for n in N:
			if n - k > 0:
				r.append((k,n, n - k))
	return r
def Deceitful(K, N, num):
	pass
	#newK = list(K)
	#newN = list(N)
	#pairs = allPossiblePair(K, N, num)
	#print pairs
	#pairs = sorted(pairs, key=lambda tup:tup[2], reverse = True)
	#point = 0
	#while True:
		#if len(pairs) == 0:
			#break
		#(sK, sN, weight) = pairs[0]
		#newPairs = []
		#for p in pairs:
			#if p[0] != sK or p[1] != sN:
				#newPairs.append(p)
		#
		#allPossiblePair[0]
	#point 
def Deceitful1(K, N, num):
	count = 0
	newK = list(K)
	newN = list(N)
	for k in K:
		if k < N[0]:
			newK.remove(k)
			newN.remove(N[-1])
			N = list(newN)
		else:
			newK.remove(k)
			newN.remove(N[0])
			N = list(newN)
			count += 1
	
	return count
for i in range(numTest):
	num = int(f.readline().strip())
	K = f.readline().strip().split()
	N = f.readline().strip().split()
	
	for j in range(num):
		K[j] = float(K[j])
		N[j] = float(N[j])
	K = sorted(K)
	N = sorted(N)

	
	#Deceitful(K, N, num)
	fAns.write('Case #'+str(i + 1) + ': ' + str(Deceitful1(K, N, num)) + ' ' + str(War(K,N, num)) + '\n')
fAns.close()
f.close()