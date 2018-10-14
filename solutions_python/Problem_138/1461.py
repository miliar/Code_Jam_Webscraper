from itertools import islice
import os

abpath = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

ANSWER_TEMPLATE = "Case #{}: {} {}"

def solve(in_path, out_path):
	case_num = 1
	test_cases = 0

	with open(in_path, "rb") as i, open(out_path, "w+b") as o:
		test_cases = int(i.readline())
		while True:
			case = list(islice(i, 3))
			if not case:
				break
			
			solution = solve_case(
				int(case[0]),
				map(float, case[1].split(' ')),
				map(float, case[2].split(' ')),
				case_num
			)
			o.write(solution)
			if case_num < test_cases:
				o.write("\n")

			case_num += 1


def solve_case(num_blocks, n_masses, k_masses, case_num):
	# pass copies to be destroyed
	deceit_solution = solve_deceit(list(n_masses), list(k_masses))	
	war_solution = solve_war(n_masses, k_masses)

	answer = ANSWER_TEMPLATE.format(case_num, deceit_solution, war_solution)
	return answer


def solve_deceit(n_masses, k_masses):
	points = 0
	n_masses.sort(reverse=True)
	k_masses.sort(reverse=True)

	idx = 0
	while n_masses:
		if n_masses[idx] > k_masses[idx]:
			points += 1
			# In reality k would use his lowest if this piece was played,
			# but this aint a simulation.
			k_masses.pop(0)
			n_masses.pop(0)
		else:
			k_masses.pop(0)
			n_masses.pop()

	return points

def solve_war(n_masses, k_masses):
	points = 0
	n_masses.sort(reverse=True)
	k_masses.sort(reverse=True)

	def smallest_winner(n_mass):
		smallest_winner = 0
		for idx, mass in enumerate(k_masses):
			if mass < n_mass:
				return smallest_winner
			else:
				smallest_winner = idx

		return smallest_winner

	idx = 0
	while n_masses:
		if n_masses[idx] > k_masses[idx]:
			points += 1
			k_masses.pop()
			n_masses.pop(0)
		else:
			k_masses.pop(smallest_winner(n_masses[0]))
			n_masses.pop(0)

	return points


if __name__ == '__main__':
	solve(abpath("D-large.in"), abpath("D-large.out"))
