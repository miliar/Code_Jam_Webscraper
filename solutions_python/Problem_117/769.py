lawn = [[0] * 100 for i in range(100)]
above_min = [[0] * 100 for i in range(100)]
below_min = [[0] * 100 for i in range(100)]
left_min = [[0] * 100 for i in range(100)]
right_min = [[0] * 100 for i in range(100)]
M=0;N=0

def set():
	for i in range(1,N):
		above_min[i][:M] = [max(j,k) for (j,k) in zip(lawn[i-1][:M],above_min[i-1][:M])]
		below_min[N-1-i][:M] = [max(j,k) for (j,k) in zip(lawn[N-i][:M],below_min[N-i][:M])]
	for i in range(N):
		for j in range(1,M):
			left_min[i][j] = max(left_min[i][j-1], lawn[i][j-1])
			right_min[i][M-1-j] = max(right_min[i][M-j], lawn[i][M-j])
def reset():
	for i in range(N):
		for j in range(M):
			lawn[i][j]=above_min[i][j] = below_min[i][j] = left_min[i][j] = right_min[i][j] = 0
def check():
	for i in range(N):
		for j in range(M):
			if (lawn[i][j]<left_min[i][j] or lawn[i][j]<right_min[i][j]) and (lawn[i][j]<below_min[i][j] or lawn[i][j]<above_min[i][j]):
				return False
	return True

T = int(raw_input())
for i in range(T):
	N,M = map(int, raw_input().split())
	for j in range(N):
		lawn[j][:M] = map(int, raw_input().split())
	set()
	if check():
		print 'Case #%d: YES' % (i+1)
	else:
		print 'Case #%d: NO' % (i+1)
	reset()
