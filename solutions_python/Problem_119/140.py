#!/usr/bin/env python

from collections import Counter

class Chest:

	def __init__(self, chest_id):

		self.chest_id = chest_id
		self.required_key = None
		self.contain_keys = None


class TreasureSolver:

	def __init__(self, init_treasure):

		self.call_stack = [init_treasure]

	def solve(self, chests):

		while len(self.call_stack) > 0:
			#print 'call stack: ', self.call_stack

			treasure = self.call_stack.pop()
			#print treasure.opened_chests, treasure.keys, treasure.future_keys, treasure.require_keys
			result = treasure.try_open(chests)
			if result is not None:
				if len(result) == 0:
					return treasure.opened_chests
				else:
					self.call_stack.extend(result)

		return None


class Treasure:

	def __init__(self):

		self.keys = Counter()
		self.opened_chests = []
		self.future_keys = Counter()
		self.require_keys = Counter()

	def set_chests(self, chests):

		for chest in chests:
			self.require_keys[chest.required_key] += 1
			for key in chest.contain_keys:
				self.future_keys[key] += 1

	def __repr__(self):

		return '<keys: %s, opened_chests: %s>' % (self.keys, self.opened_chests)

	def clone(self):

		ret = Treasure()
		ret.keys = self.keys.copy()
		ret.opened_chests = self.opened_chests[:]
		ret.future_keys = self.future_keys.copy()
		ret.require_keys = self.require_keys.copy()

		return ret

	def try_open(self, chests):

		if len(self.opened_chests) == len(chests):
			return []

		c1 = self.keys + self.future_keys
		for key in c1:
			if c1[key] < self.require_keys[key]:
				return None

		lock_chests = filter(lambda c: c.chest_id not in self.opened_chests,
							 chests)

		for chest in lock_chests:
			c2 = c1.copy()
			for key in chest.contain_keys:
				c2[key] -= 1

			if c2[chest.required_key] == 0:
				return None

		to_open = filter(lambda c: self.keys[c.required_key] > 0, lock_chests)
		if len(to_open) == 0:
			return None
		elif len(to_open) == 1:
			self.open(to_open[0])
			return [self]

		ret = []
		for chest in to_open:
			t = self.clone()
			t.open(chest)
			ret.append(t)

		ret.reverse()
		return ret

	def open(self, chest):

		self.opened_chests.append(chest.chest_id)
		self.keys[chest.required_key] -= 1
		for key in chest.contain_keys:
			self.keys[key] += 1
			self.future_keys[key] -= 1
		self.require_keys[chest.required_key] -= 1


def main():

	test_data = None
	with open('input', 'r') as f:
		test_data = f.read()

	test_data = test_data.split('\n')

	num_test = int(test_data[0])
	test_data_ix = 1
	for test in xrange(num_test):
		t = Treasure()
		chests = []

		num_keys, num_chests = map(int, test_data[test_data_ix].split(' '))
		test_data_ix += 1

		t.keys = Counter(map(int, test_data[test_data_ix].split(' ')))
		test_data_ix += 1

		for c in xrange(num_chests):
			data = map(int, test_data[test_data_ix].split(' '))
			test_data_ix += 1

			chest = Chest(c + 1)
			chest.required_key, num_contain_keys = data[0], data[1]
			chest.contain_keys = data[2:]

			chests.append(chest)

		t.set_chests(chests)
		treasure_solver = TreasureSolver(t)
		result = treasure_solver.solve(chests)
		if result is not None:
			print 'Case #%s: %s' % (test + 1, ' '.join(map(str, result)))
		else:
			print 'Case #%s: IMPOSSIBLE' % (test + 1)


def test():

	test_data = """10 20
1 2 3 4 5 6 7 8 9 10
2 0
6 1 6
1 1 1
6 0
5 1 5
1 0
8 1 8
10 1 10
9 0
7 1 7
3 0
4 1 4
10 0
8 0
3 1 3
7 0
9 1 9
2 1 2
5 0
4 0"""

	test_data = test_data.split('\n')
	test_data_ix = 0

	t = Treasure()
	chests = []

	num_keys, num_chests = map(int, test_data[test_data_ix].split(' '))
	test_data_ix += 1

	t.keys = Counter(map(int, test_data[test_data_ix].split(' ')))
	test_data_ix += 1

	for c in xrange(num_chests):
		data = map(int, test_data[test_data_ix].split(' '))
		test_data_ix += 1

		chest = Chest(c + 1)
		chest.required_key, num_contain_keys = data[0], data[1]
		chest.contain_keys = data[2:]

		chests.append(chest)

	t.set_chests(chests)
	treasure_solver = TreasureSolver(t)
	result = treasure_solver.solve(chests)


if __name__ == "__main__":
	main()