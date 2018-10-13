import fileinput
import sys
import math

# I believe special minutes should be performed at the start, then people should be let to eat.
# the split should always go to some empty plate.

# the time is equal to the time taken to split the piles of pancake + the size of the bigger stack
# splits to consider: 
# x minutes: divide one stack by x+1

# here is the deal: amount of special minutes, we start with 0 special minutes and a max time


def ex1(line):
	plates = [(int(x), int(x), 1) for x in line.split(" ")]
	plates = sorted(plates, reverse=True)
	best_time = plates[0][0]
	for special_minutes in range(1, best_time):
		# let's spend a special minute:
		# print plates
		(_, pancakes, splits) = plates[0]
		new_split_stack = math.ceil(1.0 * pancakes / (splits + 1))
		plates[0] = (int(new_split_stack), pancakes, splits + 1)
		plates = sorted(plates, reverse=True)
		best_time = min(best_time, plates[0][0] + special_minutes)
	return best_time


if __name__ == '__main__':
	max = int(sys.stdin.readline())
	for i in range(1, max + 1 ):
		sys.stdin.readline()
		print "Case #{0}: {1}".format(i, ex1(sys.stdin.readline().rstrip()))
    	
