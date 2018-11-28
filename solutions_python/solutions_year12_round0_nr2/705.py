import sys
import fileinput

def numgreater(googlers, suprising, p, totals):
	# remove googlers that can't reach p
	lowest = p + 2*(max(0,p-2))  # can't have negative scores, so cap at 0
	reachable = filter(lambda t: t >= lowest, totals)
	#print("lowest:{}, reachable: {}".format(lowest,reachable))

	# select the ones that didn't need suprising results to get p
	nosupriseneeded = p + 2*(p-1)
	needsuprise = filter(lambda t: t < nosupriseneeded, reachable)

	# left with the subset of googlers that could have got a gest result of at least p but only with a suprise
	# answer is those that didn't need a suprise, plus those of this subset that we have a suprise for
	return (len(reachable) - len(needsuprise)) + min(suprising, len(needsuprise))


count = 0
for line in fileinput.input():
	if fileinput.isfirstline():
		continue

	elems = map(int,line.split())
	googlers = elems[0]
	suprising = elems[1]
	p = elems[2]
	totals = elems[3:]

	#sys.stderr.write("googlers: {}, suprising: {}, p: {}, totals: {}\n".format(googlers,suprising,p,totals))

	answer = numgreater(googlers, suprising, p, totals)

	count += 1
	print("Case #{}: {}".format(count,answer))
