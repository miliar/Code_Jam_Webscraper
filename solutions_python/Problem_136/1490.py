from itertools import islice
import os
from decimal import Decimal, getcontext, ROUND_HALF_UP

# Set up the decimal context
getcontext().prec = 150
getcontext().rounding = ROUND_HALF_UP

abpath = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
SEVEN_PLACES = Decimal(10) ** -7
ANSWER_TEMPLATE = "Case #{}: {}"


def solve(in_path, out_path):
	case_num = 1
	test_cases = 0

	with open(in_path, "rb") as i, open(out_path, "w+b") as o:
		test_cases = int(i.readline())

		for case in i:
			case_vals = map(Decimal, case.split(' '))
			solution = solve_case(case_num, *case_vals)

			o.write(solution)
			if case_num < test_cases:
				o.write("\n")
			case_num += 1


def solve_case(case_num, cost, extra, target):
	speed = Decimal("2.0000000")
	best_time = target / speed
	elapsed = Decimal("0.0000000")

	while True:
		new_time, elapsed, speed = make_purchase(
			elapsed, speed, cost, extra, target
		)
		
		if best_time <= new_time:
			return ANSWER_TEMPLATE.format(case_num, "%0.7f" % best_time)
		else:
			best_time = new_time


def make_purchase(elapsed, speed, cost, extra, target):
	new_elapsed = elapsed + (cost / speed)
	new_speed = speed + extra
	new_time = new_elapsed + (target / new_speed)

	return new_time, new_elapsed, new_speed

if __name__ == '__main__':
	solve(abpath("B-large.in"), abpath("B-large.out"))
