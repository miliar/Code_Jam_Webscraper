import sys
import math

YES = "YES"
NO = "NO"

def main():
	f = open(sys.argv[1])
	T = int(f.readline().strip("\n"))
	for i in range (0,T):
		print "Case #%d: %s" % (i+1, isPossible(f))

def isPossible(f):
	"""determine if lawn pattern can be cut"""
	N, M = [int(s) for s in f.readline().strip("\n").split(" ")]
	board = [] * N
	for i in range(N):
		row = [int(s) for s in f.readline().strip("\n").split(" ")]
		board.append(row)

	if N==1 or M==1: return YES

	#check each column
	for i in range(M):
		column = zip(*board)[i]
		min_height = min(column)
		max_height = max(column)
		if min_height == max_height: continue
		#assume we cut at max height, all lower heights must be satisfied
		#by cutting through the row
		for j in range(N):
			if column[j] < max_height:
				#look at row, make sure nothing higher
				if(max(board[j]) > column[j]): return NO
	#passed the test, it must be okay
	return YES



if __name__ == "__main__":
	main()

