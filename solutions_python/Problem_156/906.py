import psyco
import sys
import itertools

DEBUG = False

psyco.full()

test_input = r'''3
1
3
4
1 2 1 2
1
4'''.split('\n')


def debug(s):
	if not DEBUG:
		return
	sys.stderr.write(str(s) + '\n')


def readline():
	if DEBUG:
		return test_input.pop(0)
	return raw_input()				
				


# When is it worth having a special minute?
# When one diner has x more... too hard.


def simulate(diners, minutes):

	# debug("%d\t %s" % (minutes, diners))
	
	# Stop when no diners have pancakes left.
	maxn = max(diners) if diners else 0
	if maxn == 0:
		return minutes
		
	#######################
	# No special minute.
	#######################
	
	# Subtract a pancake from each diner.
	newminutes = simulate([n - 1 for n in diners if n > 1], minutes + 1)
	#######################
	
	
	#######################
	# Special minute.
	#######################
	
	# Only take a special minute if it's worthwhile.
	if maxn > 3:
		for subamt in xrange(2, (maxn / 2) + 1):
			newdiners = [n for n in diners if n]
			
			# Find the biggest pile.
			maxi = newdiners.index(maxn)
			
			# Take some of the pancakes from the biggest pile.
			newdiners[maxi] -= subamt
			# Give it to a brand new diner.
			newdiners.append(subamt)
				
			tmins = simulate(newdiners, minutes + 1)
			if tmins < newminutes:
				newminutes = tmins
	#######################
	
	
	# Return fewest minutes from the above options.
	return newminutes

				
def case(casenum):

	num_diners = int(readline())
	pancakes = map(int, readline().split())
	
	diners = pancakes
	
	minutes = simulate(diners, 0)
	
	output = minutes

	print "Case #%d: %d" % (casenum, output)
	
	

def main():
	numcases = readline()
	for i in xrange(int(numcases)):
		case(i + 1)

main()
