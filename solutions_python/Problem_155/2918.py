# -*- coding: utf-8 -*-

from pprint import pprint


class Member:
	shyness = 0
	standing = False

	def __init__(self, shyness):
	    self.shyness = shyness


def _all_standing(audience):
	for m in audience:
		if not m.standing:
			return False

	return True


def _n_standing(audience):
	n = 0

	for m in audience:
		if m.standing:
			n += 1

	return n


def _stand_up_r(audience):
	change = False

	for m in audience:
		if m.shyness <= 0 or m.shyness <= _n_standing(audience):
			if m.standing == False:
				change = True
				m.standing = True

	if change:
		_stand_up_r(audience)


f_out = open("out.txt", mode="w")

with open("in.txt") as f_in:
	n_cases = int(f_in.readline())
	n_case = 1

	for case in f_in.readlines():
		audience = []

		case = case.split()
		s_max = int(case[0])
		people = case[1]

		for s, n in enumerate(people):
			for _ in range(int(n)):
				audience.append(Member(s))

		friends = 0

		while True:
			_stand_up_r(audience)

			if _all_standing(audience):
				f_out.write("Case #%s: %s\n" % (n_case, friends))
				break

			audience.append(Member(0))

			friends += 1

		n_case += 1

f_out.close()