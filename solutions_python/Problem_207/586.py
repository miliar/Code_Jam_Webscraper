from __future__ import division

def get_test_cases():
	t = int(raw_input())
	for test_case in range(t):
		n, r, o, y, g, b, v = map(int, raw_input().split())
		yield n, r, o, y, g, b, v


def write_output(i, output):
	print "Case #{index}: {result}".format(index=i, result=output)


def empty(pony):
	return not pony[0]


def add_pony(result, ponies, i):
	result.append(ponies[i][1])
	ponies[i][0] -= 1
	assert(ponies[i][0] >= 0)


def swap(ponies, i, j):
	ponies[i], ponies[j] = ponies[j], ponies[i]


def sort(ponies, first_color, last_color):
	ponies = sorted(ponies, reverse=True)
	if ponies[0][0] == ponies[1][0]:
		if ponies[1][1] == first_color or ponies[0][1] == last_color:
			swap(ponies, 0, 1)
	if ponies[0][0] == ponies[1][0] == ponies[2][0]:
		if ponies[2][1] == first_color:
			if ponies[2][1] == last_color:
				swap(ponies, 1, 2)
			else:
				swap(ponies, 0, 2)
	return ponies


def solve(n, r, o, y, g, b, v):
	assert(o == g == v)
	# r, y, b
	ponies = [[r, "R"], [y, "Y"], [b, "B"]]
	ponies = sorted(ponies, reverse=True)
	first_color = ponies[0][1]
	if ponies[0][0] > sum([pony[0] for pony in ponies]) - ponies[0][0]:
		return "IMPOSSIBLE"
	result = []
	
	while ponies[1][0] > ponies[2][0]:
		add_pony(result, ponies, 0)
		add_pony(result, ponies, 1)


	while any([not empty(pony) for pony in ponies]):
		for i in range(2):
			if not empty(ponies[i]):
				last_color = ponies[i][1]
				add_pony(result, ponies, i)

		ponies = sort(ponies, first_color, last_color)
		#print ponies
		#print "".join(result)


	return "".join(result)


def main():
	for i, input_data in enumerate(get_test_cases(), start=1):
		write_output(i, solve(*input_data))


if __name__ == '__main__':
	main()