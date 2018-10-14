# 
# A certain bathroom has N + 2 stalls in a single row;
# the stalls on the left and right ends are permanently 
# occupied by the bathroom guards. The other N stalls 
# are for users.
# 
# Whenever someone enters the bathroom, they try to 
# choose a stall that is as far from other people as 
# possible. 
# To avoid confusion, they follow deterministic rules: 
# For each empty stall S, they compute two values LS 
# and RS, each of which is the number of empty stalls 
# between S and the closest occupied stall to the left 
# or right, respectively. Then they consider the set of 
# stalls with the farthest closest neighbor, that is, 
# those S for which min(LS, RS) is maximal. If there is 
# only one such stall, they choose it; otherwise, they 
# choose the one among those where max(LS, RS) is 
# maximal. If there are still multiple tied stalls, they
# choose the leftmost stall among those.
# 
# K people are about to enter the bathroom; each one 
# will choose their stall before the next arrives. 
# Nobody will ever leave.
# 
# Input
# 
# The first line of the input gives the number of test 
# cases, T. T lines follow. Each line describes a test 
# case with two integers N and K, as described above.
# 
# Output
# 
# For each test case, output one line containing Case 
# x: y z, where x is the test case number (starting 
# from 1), y is max(LS, RS), and z is min(LS, RS) as 
# calculated by the last person to enter the bathroom 
# for their chosen 
# stall S.
#
# Limits 
# 1 <= T <= 100.
# 1 <= K <= N.
# Small dataset 1
# 1 <= N <= 1000.
# Small dataset 2
# 1 <= N <= 106.
# Large dataset
# 1 <= N <= 1018.
# Sample
#
# Input 
# 5
# 4 2
# 5 2
# 6 2
# 1000 1000
# 1000 1
#  	
# Output 
# Case #1: 1 0
# Case #2: 1 0
# Case #3: 1 1
# Case #4: 0 0
# Case #5: 500 499
# 
from Queue import Queue
from Queue import PriorityQueue
class Item:
	imax = 0
	imin = 0
	rep = 0
	backup = 0

	def __init__(self, imax, imin, rep):
		self.imin = imin
		self.imax = imax
		self.rep = rep
		self.backup = self.rep

	def add_rep(self, rep):
		self.rep += rep
		self.backup = self.rep

	def use(self):
		self.rep -= 1

def problem():
	inp = raw_input()
	inp = inp.split(' ')
	N = int( inp[0] )
	K = int( inp[1] )
	return get_min_max( N, K )

def get_min_max( n, k ):
	
	item_map = {}
	queue = PriorityQueue()
	item_min = ((n-1) / 2) 
	item_max = (n) / 2 

	curr_min = 0
	curr_max = 0
	curr_item = item = Item(item_max, item_min, 1)

	item_map[item_max+item_min] = item

	for person in range(k):
		if curr_item.rep == 0:
			# get next set
			curr_item = queue.get()[1]
		curr_item.use()

		# create items from current item
		# create 1 item for each value (min max)
		values = [curr_item.imax, curr_item.imin]
		for value in values:
			if value == 0:
				continue
			item_min = (value-1) / 2
			item_max = (value ) / 2
			if item_map.has_key(item_min+item_max):
				# key exist
				item_map[item_min+item_max].add_rep(1)
			else:
				# new entry
				item = Item(item_max, item_min, 1)
				item_map[item_min+item_max] = item
				queue.put([-(item_min+item_max), item])
	#let it ends
	return curr_item.imax, curr_item.imin


if __name__ == '__main__':
	T = int(raw_input())
	case = 1
	while ( T > 0 ):
		pmax, pmin = problem()
		print "Case #%s: %s %s" % ( case, pmax, pmin )
		case = case + 1
		T = T - 1
 
	
 