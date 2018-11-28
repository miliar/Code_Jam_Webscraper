import sys
import bisect

num_cases = int(sys.stdin.readline().strip())

def get_state():
	answer = int(sys.stdin.readline().strip())
	board = [map(int, sys.stdin.readline().strip().split()) for row_num in range(0, 4)]
	return answer, board
	
def play_war(n, k):
	takes = 0
	for n_piece in sorted(n):
		idx = bisect.bisect_left(k, n_piece)
		if idx > len(k) - 1:
			takes += 1
			idx = 0
		# print n_piece, k[idx]
		k.pop(idx)
	return takes
	
def play_deceitful_war(n, k):
	takes = 0
	while n:
		# while naomi has some blocks that she can never get anything with, tell ken something just under his highest so he'll put his highest down and she'll toss her worst
		while(n and n[0] < k[0]):
			k.pop()
			n.pop(0)
		# after that, keep calling out a weight that's bigger than ken's. he'll always put his lowest down and you can take it with your lowest 
		while(n and n[0] > k[0]):
			k.pop(0)
			n.pop(0)
			takes += 1
	return takes
		
for i in range(num_cases):
	num_blocks = int(sys.stdin.readline().strip())
	n_weights = sorted(map(float, sys.stdin.readline().strip().split()))
	k_weights = sorted(map(float, sys.stdin.readline().strip().split()))
	#print n_weights
	#print k_weights

	w = play_war(n_weights[:], k_weights[:])
	dw = play_deceitful_war(n_weights[:], k_weights[:])

	print "Case #%s: %s %s" % (i+1, dw, w)