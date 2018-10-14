import sys
ATTEMPT_NO = 0
ATTEMPT_TYPE = "small"

""" Basic logic:
We must make a decision at each point we have
enough to buy a new farm. Do we buy, or do we
hold out.

At each iteration we have:
	rate = F*(n_farms + 2)
	t_next_decision = (C - current)/rate
	wallet += (F*n_farms + 2)*t_next_decision

We check if: time_to_win_with_farm > time_to_win_without_farm
	rate_with = F*(n_farms + 1) + 2
	t_with = (X - (wallet - C))/rate_with

	rate_without = rate
	t_without = (X - wallet)/rate_without
"""

def solve(C, F, X):
	done = False
	wallet = float(0)
	time = float(0)
	n_farms = 0

	while not done:
		rate = F*n_farms + 2
		t_next_decision = min((C - wallet)/rate, (X - wallet)/rate)
		wallet += rate*t_next_decision
		time += t_next_decision

		# Get time to win with and without a new farm
		rate_with = F*(n_farms + 1) + 2
		t_with = (X - (wallet - C))/rate_with
		t_without = (X - wallet)/rate

		if t_with < t_without:
			n_farms += 1
			wallet -= C
		else:
			time += t_without
			done = True
	return time


if __name__ == '__main__':
	#f = open("B-%s-attempt%d.in" % (ATTEMPT_TYPE, ATTEMPT_NO))
	#sys.stdout = open("B-%s-attempt%d.out" % (ATTEMPT_TYPE, ATTEMPT_NO), "w+")

	f = open("B-large.in")
	sys.stdout = open("B-large.out", "w+")
	T = int(f.readline())

	for i in range(1, T + 1):
		C, F, X = [float(x) for x in f.readline().split()]
		result = solve(C, F, X)
		print("Case #%d: %.8f" % (i, result))