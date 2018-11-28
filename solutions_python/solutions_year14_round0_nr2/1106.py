
import sys

sys.setrecursionlimit(100000000)

def step_r(time_used, cookies, per_sec, GOAL, FARM_COST, FARM_EXTRA):
	just_wait = GOAL / per_sec
	time_for_farm = FARM_COST / per_sec

	if just_wait > time_for_farm + (GOAL / (per_sec + FARM_EXTRA)):
		return step_r(time_used + time_for_farm, 0, per_sec + FARM_EXTRA, GOAL, FARM_COST, FARM_EXTRA)

	return time_used + just_wait


in_file = open("B-small-attempt0.in")
out_file = open("B-small-attempt0.out", "wt")

# Skip first line
in_file.readline()

C, F, X, result, case = None, None, None, None, 0

for line in in_file:
	case += 1
	line = line.split()

	C = float(line[0])
	F = float(line[1])
	X = float(line[2])

	result = step_r(0, 0, 2, X, C, F)

	print("Case #%s: %s" % (case, "{0:.7f}".format(result)))
	out_file.write("Case #%s: %s\n" % (case, "{0:.7f}".format(result)))

in_file.close()
out_file.close()