import sys

def is_ok(people, additional):
	total = people[0] + additional
	for idx in range(1, len(people)):
		if idx <= total:
			total += people[idx]
		else:
			return False
	return True

def solve(people_str):
	people = [int(i) for i in people_str]
	for additional in range(len(people)):
		if is_ok(people, additional):
			return additional
	raise 'Must not happen'

def parse(input_str):
	return [line.split(' ')[1].rstrip() for line in input_str[1 :] if line != '']

# input_str = """4
# 4 11111
# 1 09
# 5 110011
# 0 1"""

parsed = parse(sys.stdin.readlines())
for idx in range(len(parsed)):
	print("Case #%d: %d" % (idx + 1, solve(parsed[idx])))

# print(solve('11111'))
# print(solve('09'))
# print(solve('110011'))
# print(solve('1'))

