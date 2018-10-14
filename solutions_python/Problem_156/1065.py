#brute force 

from collections import defaultdict

memo = defaultdict(int)

def get_max(plates):
	for pancakes, multiplicity in reversed(list(enumerate(plates))):
		if multiplicity > 0:
			return (multiplicity, pancakes)

def generate(plates, div):
	_, pancakes = get_max(plates)
	h = list(plates)
	h[pancakes] -= 1
	split = int(pancakes/div)
	h[split] += 1
	h[pancakes - split] += 1
	return h

def solve(plates, special):
	multiplicity, pancakes = get_max(plates)
	time = pancakes + special
	#print(str(plates) + ' ' + str(time))
	if pancakes == 2:
		return time
	for i in range(2,4):
		if i >= pancakes:
			break
		h = generate(plates, i)
		if memo[tuple(h)] == 0:
			memo[tuple(h)] = solve(h, special + 1)

		if memo[tuple(h)] < time:
			time = memo[tuple(h)]
	return time

def pancakes():
	with open('input.in','r') as f, open('output.out','w') as w:
		T = int(f.readline())
		for case in range(T):
			special_time = 0
			diners = int(f.readline())
			plates = [0] * 10
			cache = [int(p) for p in f.readline().split(' ')]
			for i in cache:
				plates[i] += 1

			special = 0
			if memo[tuple(plates)] == 0:
				memo[tuple(plates)] = solve(plates, special)
			
			time = memo[tuple(plates)]
			memo.clear() #having some weird  

			w.write('Case #' + str(case+1) + ': ' + str(time) + '\n')
			print('Case #' + str(case+1) + ': ' + str(time) + ' ' + str(cache))
pancakes()
