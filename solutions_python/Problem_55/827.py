import sys
from collections import deque

def main(argv):
	input_file = open(argv[1], "r")
	
	T = int(input_file.readline())
	
	for t in range(1, T + 1):
		# read values
		(R, k, n) = [int(k) for k in input_file.readline().split()]
		G = [int(g) for g in input_file.readline().split()]
		G_ = deque(G)
		
		# run the roller coaster R times
		total_amount = 0
		for r in range(0, R):
			groups_on_board = []
			
			# fit as many people as possible
			while sum(groups_on_board) <= k and len(G_) > 0:
				g = G_.popleft()
				groups_on_board.append(g)
				
			if sum(groups_on_board) > k:
				G_.appendleft(groups_on_board[-1])
				del groups_on_board[-1]
			
			total_amount += sum(groups_on_board)
			
			for g in groups_on_board:
				G_.append(g)
				
		print "Case #%d: %d" % (t, total_amount)
			
	
if __name__ == "__main__":
	main(sys.argv)
