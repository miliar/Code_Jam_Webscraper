T = int(input())

for t in range(T):
	order = 'ROYGBV'
	solution = []
	unicorn_string = input().split(' ')
	unicorns = []
	impossible = True
	'''red = (6,0,1)
	blue = (3,4,5)
	yellow = (1,2,3)
	'''
	N = int(unicorn_string[0])
	
	for number in unicorn_string[1:]:
		unicorns.append(int(number))
	
	max_index = unicorns.index(max(unicorns))
	longest = unicorns[max_index]
	
	for i in range(longest):
		solution.append(order[max_index])
	unicorns[max_index] = 0
	
	if sum(unicorns)<longest:
		print('Case #{}: {}'.format(t+1,'IMPOSSIBLE'))
		continue
		
	max_index = unicorns.index(max(unicorns))
	longest = unicorns[max_index]
	current_length = len(solution)
	
	for i in range(longest):
		solution.insert(current_length-i,order[max_index])
	unicorns[max_index] = 0
	
	max_index = unicorns.index(max(unicorns))
	longest = unicorns[max_index]
	
	for i in range(longest):
		solution.insert(2*i+1,order[max_index])
	unicorns[max_index] = 0
	
	solution = ''.join(solution)
	
	print('Case #{}: {}'.format(t+1,solution))