from ucb import interact
f = open('treasure.in')
num_tests = int(f.readline())
test_number = 0

class Chest(object):
	"""docstring for Chest"""
	def __init__(self, keyToOpen, keysContained, number):
		self.keyToOpen = keyToOpen
		self.keysContained = keysContained
		self.number = number

	def canOpenWith(self, keys):
		return self.keyToOpen in keys

	def __str__(self):
		return str(self.number)

	def __repr__(self):
		return "Chest #" + str(self.number)


lookup = {}
def cache(f):
	def cached_func(chests, keys):
		item = (tuple(chests), tuple(keys))
		if item in lookup:
			return lookup[item]
		result = f(chests, keys)
		lookup[item] = result
		return result
	return cached_func

# @cache
def findChain(chests, keys = []):
	if len(keys) == 0 and len(chests) != 0:
		return False

	openable = []
	for chest in chests:
		if chest.canOpenWith(keys):
			openable.append(chest)

	if len(openable) == 0:
		return False

	for chest in openable:
		newChests = list(chests)
		newChests.remove(chest)
		newKeys = list(keys)
		newKeys.remove(chest.keyToOpen)
		newKeys += chest.keysContained
		newKeys = sorted(newKeys)

		if len(newChests) == 0:
			return [chest]

		result = findChain(newChests, newKeys)
		if result:
			return [chest] + result

	#interact()
	return False

findChain = cache(findChain)

for i in range(num_tests):
	lookup = {}
	test_number += 1
	total = 0
	chests = []
	keyChest = f.readline().split()
	numKeys = int(keyChest[0])
	numChests = int(keyChest[1])
	keys = [int(x) for x in f.readline().split()]
	
	for c in range(numChests):
		chestData = f.readline().split()
		chests.append(Chest(int(chestData[0]), [int(x) for x in chestData[2:]], c + 1))

	result = findChain(chests, keys)
	if not result:
		toPrint = "IMPOSSIBLE"
	else:
		toPrint = str(result[0])
		for elem in result[1:]:
			toPrint += " " + str(elem)

	print("Case #{0}: {1}".format(test_number, toPrint))