from datetime import datetime

input_file_path = 'A-large.in.txt'

def flip_last_k_cakes(l, k):
	for i in range(1,k+1):
		if l[-i] == '+':
			l[-i] = '-'
		else:
			l[-i] = '+'
	return l


start = datetime.now()

with open(input_file_path) as f:
	lines = f.read().splitlines()
	for j in range(1,int(lines[0])+1):
		s = lines[j].split(' ')[0]
		k = int(lines[j].split(' ')[1])
		input = list(s)
		count = 0
		done = False
		while(not done):
			if len(input) == 0:
				done = True
			else:
				x = input[-1]
				if x == '+':
					input.pop()
				elif len(input)>= k:
					count = count +1
					input = flip_last_k_cakes(input, k)
				elif len(input)< k:
					done = True		# impossible now

		if len(input) == 0:
			print 'Case #' + str(j) + ': ' + str(count)
		else:
			print 'Case #' + str(j) + ': IMPOSSIBLE'


diff = datetime.now() - start
#print diff