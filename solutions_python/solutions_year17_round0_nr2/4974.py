T = int(input())
count = 1
def check(A):
	for i in range(0, len(A)-1):
		if A[i] > A[i+1]:
			return False
	return True
while T:
	X = list(input())
	A = [int(x) for x in X]
	if check(A):
		X1 = [str(x) for x in A]
		N = ''.join(X1)
		print ("Case #"+str(count)+":", N)
	else:
		i = len(A)-2
		A[len(A)-1] = 9
		while True:
			if i > 0 and A[i] > A[i-1]:
				A[i] -= 1
				X1 = [str(x) for x in A]
				N = ''.join(X1)
				print ("Case #"+str(count)+":", int(N))
				break
			elif i == 0:
				A[i] -= 1
				X1 = [str(x) for x in A]
				N = ''.join(X1)
				print ("Case #"+str(count)+":", int(N))
				break
			else:
				A[i] = 9
				i -= 1
	count += 1
	T -= 1