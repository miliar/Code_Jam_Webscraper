def solve(pancakes,spatula):
	flipcounter = 0
	for i in range(len(pancakes)-spatula+1):
		if not pancakes[i]:
			pancakes = flip(pancakes,i,i+spatula)
			flipcounter += 1
			
	if correct(pancakes):
		return flipcounter
	else:
		return -1
		
def correct(pancakes):
	for p in pancakes:
		if not p:
			return False
			
	return True
			
def flip(pancakes, start, end):
	new_pancakes = list(pancakes)
	for i in range(start,end):
		new_pancakes[i] = not new_pancakes[i]
		
	return new_pancakes
	

cases = int(input())

for i in range(cases):
	pancakes = []
	state = input().split(" ")
	spatula = int(state[1])
	for c in state[0]:
		if c == '+':
			pancakes.append(True)
		elif c == '-':
			pancakes.append(False)
			
	solution = solve(pancakes,spatula)
	if solution == -1:
		print('Case #{}: IMPOSSIBLE'.format(i+1))
	else:
		print('Case #{}: {}'.format(i+1,solution))
	