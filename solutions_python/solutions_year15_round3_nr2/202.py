from collections import Counter

def mat_mul(A, B):
	n = len(A)
	C = [[0 for i in xrange(n)] for j in xrange(n)]
	for i in xrange(n):
		for j in xrange(n):
			for k in xrange(n):
				C[i][j] += A[i][k] * B[k][j]
	return C

def mat_exp(A, n):
	if n == 1:
		return A
	if n == 2:
		return mat_mul(A, A)
	An_2 = mat_exp(A, n/2)
	An = mat_mul(An_2, An_2)
	if n%2 == 1:
		An = mat_mul(An, A)
	return An


def solve(case, K, L, S):
	K = Counter(K)
	lk = sum(K.values())
	for c in L:
		if c not in K:
			return 0
	longest_suffix = 0
	for ls in xrange(len(L)-1, 0, -1):
		if L[len(L)-ls:len(L)] == L[:ls]:
			longest_suffix = ls
			break
	max_bananas = (S - len(L)) / (len(L) - longest_suffix) + 1
	t_matrix = [[0 for i in xrange(len(L)+1)] for j in xrange(len(L)+1)]
	t_matrix[0][1] = K[L[0]]/(1.0 * lk)
	t_matrix[0][0] = 1-t_matrix[0][1]
	for i in xrange(1, len(L)+1):
		sum_t = 0
		for c in K.keys():
			for j in xrange(min(i+1,len(L)), 0, -1):
				if c != L[j-1]:
					continue
				if L[i-j+1:i] == L[:j-1]:
					t_matrix[i][j] = K[c]/(1.0 * lk)
					sum_t += t_matrix[i][j]
					break
		t_matrix[i][0] = 1-sum_t
	c_mat = [[t_matrix[i][j] for j in xrange(len(L)+1)] for i in xrange(len(L)+1)]
	val = 0
	for p in xrange(S):
		val += c_mat[0][len(L)]
		c_mat = mat_mul(c_mat, t_matrix)
	return max_bananas - val

T = int(raw_input())
for case in xrange(1, T+1):
    K, L, S = map(int, raw_input().split())
    k = raw_input()
    l = raw_input()
    print "Case #{}: {}".format(case, solve(case, k, l, int(S)))