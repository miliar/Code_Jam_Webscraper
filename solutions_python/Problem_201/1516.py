import sys

# WARNING: Assumes all input is squeaky clean.

def main():
	T = int(input())

	for case_num in range(1,T+1):
		N, K = [int(num) for num in input().split(' ')]

		i = 1
		interval = split(N)
		dyn = {}
		increment(dyn, interval)
		while i < K:
			interval = get_best_interval(dyn)
			decrement(dyn, interval)
			if (interval != (0,0)):
				increment(dyn, split(interval[0]))
				increment(dyn, split(interval[1]))
			i += 1

		interval = get_best_interval(dyn)
		y, z = max(interval), min(interval)
		print("Case #{0}: {1} {2}".format(case_num, y, z))

# TODO: could be made more efficient by making dyn a different datastructure.
def get_best_interval(dyn):
	best = (0, 0)
	bestset = set()
	bestset.add(best)

	# find maximal min(interval)
	for interval in dyn.keys():
		if min(interval) > min(best):
			best = interval
			bestset.clear()
			bestset.add(interval)
		elif min(interval) == min(best):
			bestset.add(interval)
	
	# tiebreaker max(Ls, Rs) out of maximal min(interval)
	if len(bestset) > 1:
		best = bestset.pop()
		for interval in bestset:
			if max(interval) >  max(best):
				best = interval
		return best
	else:
		return bestset.pop()

def split(N):
	if (N > 1):
		Ls = int((N-1) / 2)
		Rs = (N-1) - Ls
		return (Ls, Rs)
	else:
		return (0, 0)

def increment(dyn, interval):
	if interval in dyn:
		dyn[interval] += 1
	else:
		dyn[interval] = 1

def decrement(dyn, interval):
	if interval in dyn:
		if dyn[interval] <= 1:
			dyn.pop(interval, None)
		else:
			dyn[interval] -= 1

if __name__ == "__main__":
	main()