import hashlib
def load_setup():
	k, n = [int(x) for x in raw_input().split()]
	keys = {}
	locks = []
	rewards = []
	key_list = [int(x) for x in raw_input().split()]
	for key in key_list:
		count = keys.get(key, 0)
		keys[key] = count + 1
	for i in range(0, n):
		inputs = [int(x) for x in raw_input().split()]
		locks.append(inputs[0])
		rewards.append(inputs[2:])
	return keys, locks, rewards

def search(keys, locks, rewards, opened, seen_hashes, count, max_count):
	if count == 0:
		return ' '.join([str(x+1) for x in opened])
	current_hash = str(hash(frozenset(keys))) + str(hash(frozenset(opened)))
	#print keys, opened, seen_hashes, current_hash, count
	if current_hash in seen_hashes:
		return None
	else:
		seen_hashes.add(current_hash)

	for i in range(0, max_count):
		key = locks[i]
		if not i in opened and key in keys:
			new_keys = dict(keys)
			new_count = new_keys[key] - 1
			if new_count:
				new_keys[key] = new_count
			else:
				del new_keys[key]
			for reward in rewards[i]:
				new_count = new_keys.get(reward, 0)
				new_keys[reward] = new_count + 1
			new_opened = list(opened)
			new_opened.append(i)
			result = search(new_keys, locks, rewards, new_opened, seen_hashes, count-1, max_count)
			if result:
				return result
	return None

t = int(raw_input())
for i in range(0, t):
	keys, locks, rewards = load_setup()
	result = search(keys, locks, rewards, [], set(), len(locks), len(locks))
	if result is None:
		result = 'IMPOSSIBLE'
	print 'Case #%s: %s' % (i+1, result)
