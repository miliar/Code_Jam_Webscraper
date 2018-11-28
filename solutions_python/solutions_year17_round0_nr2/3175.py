T = int(raw_input().strip())
def naive_test(N):
	n = int(''.join(map(str,N)))
	for i in range(n, -1, -1):
		if is_tidy(i):
			return i

def is_tidy(n):
	n = map(int, list(str(n)))
	tidy = True
	for i in range(len(n)-1):
		if n[i] > n[i+1]:
			return False
	return tidy

for t in range(1,T+1):
	N = map(int, list(raw_input().strip()))
	if len(N) > 1 and not is_tidy(int(''.join(map(str,N)))):

		A = [0]*len(N)
		A[-1] = 9

		for i in range(len(N)-2,-1,-1):
			if A[i+1] > N[i+1] and N[i] != 0:
				A[i] = N[i] - 1
			elif A[i+1] > N[i+1] and N[i] == 0:
				A[i] = 9			
			else:
				A[i] = N[i]

			if A[i] > A[i+1]:
				A[i+1] = 9
				A[i] -= 1

		ans = ''.join(map(str,A))
		ans = ans.lstrip('0')
	else:				
		ans = ''.join(map(str, N))
	naive = naive_test(N)	
	print 'Case #{0}: {1}'.format(t, ans)

