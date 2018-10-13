import sys

def parse_cases(fh):
	for _ in xrange(int(next(fh))):
		yield map(float,next(fh).split())


def solve_case(farm_cost, farm_rate, cookie_goal):
	cps = 2.0
	last_goal_sec = cookie_goal / cps
	last_cum_farm_sec = 0
	while True:
		cum_farm_sec = last_cum_farm_sec + (farm_cost / cps)
		cps += farm_rate
		goal_sec = cookie_goal / cps
		soln = last_goal_sec + last_cum_farm_sec
		if soln < goal_sec + cum_farm_sec:
			return soln
		last_goal_sec = goal_sec
		last_cum_farm_sec = cum_farm_sec


def main():
	for i,case in enumerate(parse_cases(sys.stdin)):
		print "Case #%d: %.7f" % (i+1, solve_case(*case))


if __name__ == '__main__':
	main()
