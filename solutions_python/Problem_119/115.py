import sys

f = sys.stdin

def readline():
	l = f.readline().strip()
	# print l
	return l

class Game:
	def __init__(self, keys, chests, depth):
		self.chests = chests
		self.keys = keys
		self.result = []
		self.must_open = self.get_must_open()
		self.depth = depth
		# self.quick_open()

	def quick_open(self):
		remaining_chests = [c for c in self.chests if c.is_opened == False]

		indexes = []
		for c in remaining_chests:
			if c.open_key in self.keys:
				indexes.append(c.index)

		indexes = sorted(indexes)

		flag = False
		for index in indexes:
			if index in self.must_open:
				self.open_index(index)
				flag = True
			else:
				return False

		if flag:
			self.quick_open()
			pass

		return True

	def quick_check_fail(self):
		if not self.can_open():
			return True

		remaining_chests = [c.clone() for c in self.chests if c.is_opened == False]
		keys = set(self.keys)

		if len(keys) == 0 and len(remaining_chests) > 0:
			return True

		flag = True
		while flag:
			flag = False
			for c in remaining_chests:
				if c.open_key in keys and c.is_opened == False:
					c.is_opened = True
					flag = True
					for k in c.keys:
						keys.add(k)

		for c in remaining_chests:
			if c.is_opened == False:
				return True
		return False

		for c in self.chests:
			if c.is_opened == False:
				try:
					keys.remove(c.open_key)
				except ValueError:
					return True


	def can_open(self):
		keys = [k for k in self.keys]
		chests = [c for c in self.chests if not c.is_opened]

		for c in chests:
			for k in c.keys:
				keys.append(k)

		for c in chests:
			try:
				keys.remove(c.open_key)
			except ValueError:
				return False

		return True

	def is_done(self):
		for c in self.chests:
			if c.is_opened == False:
				return False
		return True

	def open_index(self, index):
		c = self.get_chest(index)
		self.open_chest(c)

	def open_chest(self, chest):
		chest.is_opened = True
		self.result.append(chest.index)
		self.keys.remove(chest.open_key)
		for key in chest.keys:
			self.keys.append(key)
		
		self.must_open = self.get_must_open()

	def get_chest(self, index):
		chests = [c for c in self.chests if c.index == index]
		if len(chests) != 1:
			raise Exception("Error")
		return chests[0]

	def get_must_open(self):
		keys = set(self.keys)
		chests = set()
		for key in keys:
			key_count = len([k for k in self.keys if k == key])
			openable_chest = [c for c in self.chests if c.open_key == key and c.is_opened == False]
			chest_count = len(openable_chest)
			if key_count >= chest_count and chest_count > 0:
				for c in openable_chest:
					chests.add(c.index)

		for c in self.chests:
			if c.is_opened == False and c.open_key in c.keys and c.open_key in keys:
				chests.add(c.index)
		return chests

	def try_open(self):
		remaining_chests = [c for c in self.chests if not c.is_opened]

		indexes = []
		for c in remaining_chests:
			if c.open_key in self.keys:
				indexes.append(c.index)

		indexes = sorted(indexes)
		game_result = None

		for index in indexes:
			c = self.get_chest(index)

			keys = [k for k in self.keys]
			keys.remove(c.open_key)
			keys = keys + c.keys

			chests = [x.clone() for x in remaining_chests if x.index != index]

			game = Game(keys, chests, self.depth + 1)
			game.run(index)

			if game.is_done():
				self.open_index(index)

				for index in game.result:
					self.open_index(index)
				return

	def run(self, tmp):
		if self.is_done():
			return " ".join(map(str, self.result))

		if self.quick_check_fail():
			return "IMPOSSIBLE"

		self.try_open()

		if self.is_done():
			return " ".join(map(str, self.result))

		return "IMPOSSIBLE"


class Chest:
	def __init__(self, index, open_key, keys):
		self.index = index
		self.open_key = open_key
		self.keys = [k for k in keys if k != 0]
		self.is_opened = False

	def clone(self):
		return Chest(self.index, self.open_key, [k for k in self.keys])

	def __str__(self):
		return str(self.index)

def read_game(f):
	keys = []
	chests = []
	key_count, chest_count = readline().split(" ")

	key_count = int(key_count)
	chest_count = int(chest_count)
	keys = readline().split(" ")
	keys = map(int, keys)

	for i in range(1, chest_count + 1):
		chest_keys = readline().split(" ")
		chest_keys = map(int, chest_keys)
		c = Chest(i, chest_keys[0], chest_keys[2:])
		chests.append(c)
	return keys, chests

def main():
	game_count = int(f.readline())
	for i in range(1, game_count + 1):
		keys, chests = read_game(f)
		game = Game(keys, chests, 0)
		result = game.run(0)
		print "Case #%d: %s" % (i, result)

main()