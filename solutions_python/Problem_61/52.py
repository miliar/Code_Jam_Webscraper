
choose_memo = {}
def choose(n,k):
	return choose1(n,k,choose_memo)

def choose1(n,k,memo):
	if k == 0: return 1
	if k == n: return 1
	if n == 0: return 0
	if not memo.has_key((n,k)):
		memo[(n,k)] = choose1(n-1,k,memo) + choose1(n-1,k-1,memo)
	return memo[(n,k)]


# Let dp[i][j] be the number of PURE sequences of ending in i, of length j
#   Obviously i > j (since all pure sequences are increasing)
# dp[x][1] = 1 for all x
# dp[x][x-1] = 1 for all x
# dp[i][j] 

ways_memo = {}
def ways(i,j):
	return ways1(i,j,ways_memo)

def ways1(i,j,memo):
	if i <= j or i == 0 or j == 0:
		return 0
	if j == 1 or i-j==1:
		return 1
	if not memo.has_key((i,j)):
		memo[(i,j)] = sum([ ways(j,k) * choose(i-j-1, j-k-1) for k in range(1,j)])
	return memo[(i,j)]
	
	
answers = {}
for i in range(502):
	answers[i] = sum(ways(i,j) for j in range(1,i))
	#Man, I should just save this in a file.  ;P
	#print "%d : %d" % (i, (answers[i]%100003))
	

# PRECOMPUTATION OVER.  PROCESS INPUT.

T = int(raw_input().strip())
for case in range(1,T+1):

	X = int(raw_input().strip())
	print "Case #%d: %d" % (case, (answers[X] % 100003))
