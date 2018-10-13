from math import floor
from heapq import heappush, heappop


def main():
	n_cases = int(raw_input())
	for i in xrange(n_cases):
		n_stalls, n_people = map(int, raw_input().split())
		max_l_r, min_l_r = last_l_r(n_stalls, n_people)
		print "Case #%d: %d %d" % (i + 1, max_l_r, min_l_r)


def last_l_r(n_stalls, n_people):
	stalls =[0] * (n_stalls + 2)
	stalls[0] = 1
	stalls[-1] = 1

	gaps = []
	heappush(gaps, (len(stalls) - 1, 0, len(stalls) - 1))

	for i in xrange(n_people):
		_, left, right = heappop(gaps)
		pos = int(floor((left + right) / 2.0))
		stalls[pos] = 1
		heappush(gaps, (-(pos - left), left, pos))
		heappush(gaps, (-(right - pos), pos, right))

	l_r = (pos - left - 1, right - pos - 1)
	return max(l_r), min(l_r)


def test_example_1():
	assert last_l_r(4, 2) == (1, 0)


def test_example_2():
	assert last_l_r(5, 2) == (1, 0)


def test_example_3():
	assert last_l_r(6, 2) == (1, 1)


def test_example_4():
	assert last_l_r(1000, 1000) == (0, 0)


def test_example_5():
	assert last_l_r(1000, 1) == (500, 499)


if __name__ == '__main__':
	main()
