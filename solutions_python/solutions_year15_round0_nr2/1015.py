import math
import sys
sys.setrecursionlimit(10000)

def pancakes(diners, minute, maxminute):

	# this is worse than having all regular minutes
	if(minute > maxminute):
		return maxminute

	# all pancakes eaten, we're done
	if all(p <= 0 for p in diners):
		return minute


	# special minute - find diner with max number of pancakes and move half
	max_p = max(diners)
	if max_p <= 3:
		return minute + max_p
	max_index = diners.index(max_p)
	special = diners[:]
	split = max_p/2
	special[max_index] = split
	special.append(max_p - split)

	distribute = diners[:]
	square = int(math.ceil(math.sqrt(max_p)))
	distribute[max_index] = max_p % square
	distribute.extend([square]*(square-1))

	# regular minute
	diners = [d-1 for d in diners]

	return min(pancakes(diners, minute+1, maxminute), pancakes(special, minute+1, maxminute), pancakes(distribute, minute + (square-1), maxminute))


		
output = open('out.txt', 'w')
with open("B-small-attempt5.in") as f:
	numtests = f.readline()
	for case in xrange(int(numtests)):
		d = f.readline()
		p = f.readline().rstrip()
		input = map(int, p.split(" "))
		max_val = max(input)
		output.write("Case #"+str(case+1)+": "+str(pancakes(input, 0, max_val))+"\n")

